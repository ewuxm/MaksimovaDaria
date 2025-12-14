import tensorflow as tf
import matplotlib.pyplot as plt


# ===== КЛАСС NEURAL STYLE TRANSFER =====

class NeuralStyleTransfer:
    def __init__(self, content_layers, style_layers):
        self.content_layers = content_layers
        self.style_layers = style_layers

        vgg = tf.keras.applications.VGG19(
            include_top=False,
            weights='imagenet'
        )
        vgg.trainable = False

        outputs = [
            vgg.get_layer(name).output
            for name in (self.style_layers + self.content_layers)
        ]
        self.model = tf.keras.Model(vgg.input, outputs)

        self.num_style = len(self.style_layers)
        self.num_content = len(self.content_layers)

    def preprocess(self, img):
        img = tf.image.resize(img, (224, 224))
        img = tf.keras.applications.vgg19.preprocess_input(img)
        return img

    def gram_matrix(self, tensor):
        # tensor: (1, h, w, c)
        result = tf.linalg.einsum('bijc,bijd->bcd', tensor, tensor)
        h = tf.shape(tensor)[1]
        w = tf.shape(tensor)[2]
        n = tf.cast(h * w, tf.float32)
        return result / n

    def _extract_features(self, image):
        img = tf.expand_dims(self.preprocess(image), 0)
        outputs = self.model(img)

        style_outputs = outputs[:self.num_style]
        content_outputs = outputs[self.num_style:]

        # Считаем Gram-матрицы только здесь
        style_features = [self.gram_matrix(o) for o in style_outputs]
        content_features = [o for o in content_outputs]
        return style_features, content_features

    def content_loss(self, content_features, generated_features):
        loss = 0.0
        for c, g in zip(content_features, generated_features):
            loss += tf.reduce_mean(tf.square(c - g))
        return loss

    def style_loss(self, style_features, generated_features):
        # На вход уже приходят Gram-матрицы, повторно gram_matrix не вызываем
        loss = 0.0
        for s_gram, g_gram in zip(style_features, generated_features):
            loss += tf.reduce_mean(tf.square(s_gram - g_gram))
        return loss

    def total_loss(self, content_image, style_image, generated_image,
                   content_weight=1e4, style_weight=1e-2):
        style_targets, content_targets = self._extract_features(style_image)
        gen_style, gen_content = self._extract_features(generated_image)

        c_loss = self.content_loss(content_targets, gen_content)
        s_loss = self.style_loss(style_targets, gen_style)
        total = content_weight * c_loss + style_weight * s_loss
        return total, c_loss, s_loss

    def transfer_style(self, content_image, style_image,
                       epochs=500,
                       content_weight=1e4,
                       style_weight=1e-2,
                       lr=0.02):
        generated = tf.Variable(tf.identity(content_image), dtype=tf.float32)
        opt = tf.keras.optimizers.Adam(learning_rate=lr)

        for epoch in range(epochs):
            with tf.GradientTape() as tape:
                loss, c_loss, s_loss = self.total_loss(
                    content_image, style_image, generated,
                    content_weight=content_weight,
                    style_weight=style_weight
                )

            grads = tape.gradient(loss, generated)
            opt.apply_gradients([(grads, generated)])

            if epoch % 100 == 0:
                print(
                    f"epoch {epoch}: "
                    f"total={loss.numpy():.2f}, "
                    f"content={c_loss.numpy():.2f}, "
                    f"style={s_loss.numpy():.2f}"
                )

        return generated


# ===== ЗАГРУЗКА И ВИЗУАЛИЗАЦИЯ ИЗОБРАЖЕНИЙ =====

def load_image(path, max_dim=512):
    img = tf.keras.utils.load_img(path)
    img = tf.keras.utils.img_to_array(img)
    long_dim = max(img.shape[:2])
    scale = max_dim / long_dim
    new_shape = (int(img.shape[0] * scale), int(img.shape[1] * scale))
    img = tf.image.resize(img, new_shape)
    return tf.cast(img, tf.float32)


def show_image(tensor, title=None):
    img = tf.cast(tensor, tf.uint8)
    plt.imshow(img.numpy())
    plt.axis("off")
    if title:
        plt.title(title)
    plt.show()


# ===== НАСТРОЙКА СЛОЁВ VGG19 =====

content_layers = ['block5_conv2']
style_layers = [
    'block1_conv1',
    'block2_conv1',
    'block3_conv1',
    'block4_conv1',
    'block5_conv1'
]

# ===== ГЛАВНЫЙ КОД ДЛЯ COLAB =====

content_path = "/content/content.jpg"
style_path = "/content/style.jpg"

content_img = load_image(content_path)
style_img = load_image(style_path)

print("Content image:")
show_image(content_img, "Content")
print("Style image:")
show_image(style_img, "Style")

nst = NeuralStyleTransfer(content_layers, style_layers)

styled = nst.transfer_style(
    content_image=content_img,
    style_image=style_img,
    epochs=500,
    content_weight=1e4,
    style_weight=1e-2,
    lr=0.02
)

print("Result:")
show_image(styled, "Styled image")

tf.keras.preprocessing.image.save_img(
    "/content/styled_result.png",
    tf.cast(styled, tf.uint8)
)
print("Сохранено в /content/styled_result.png")
