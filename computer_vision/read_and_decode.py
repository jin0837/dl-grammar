#画像データの読み込み
import tensorflow as tf
def read_and_decode(filename, reshape_dims):
    #ファイルを読み込む
    img = tf.io.read_file(filename)
  　#圧縮された文字列を3次元のunit8のテンソルに変換する
    img = tf.image.decode_jpeg(img, channels=3)
    #3次元のunit8を[0,1]の範囲の浮動小数点に変換する
    img = tf.image.convert_image_dtype(img, tf.float32)
    #画像を必要なサイズにリサイズする
    return tf.image.resize(img, reshape_dims)
