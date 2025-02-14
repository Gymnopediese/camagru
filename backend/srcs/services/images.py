

from PIL import Image
import io



def merge_images(final_path, background_image, sticker_url, position):
    
    sticker_url = sticker_url.replace("#", "/")
    background = Image.open((io.BytesIO(background_image.read())))
    sticker = Image.open("images/" + sticker_url)
    sticker = sticker.resize((sticker.size[0]//2, sticker.size[1]//2))
    background.paste(sticker, position, sticker)
    background.save(final_path)

    return final_path

if __name__ == '__main__':

    merge_images("test.png", background_image=open("images/publications/me_20250213155926833959.jpg", "rb"), sticker_url="emojis/man-getting-massage.png", position=(100, 100))
    
else:
    from imports.main import *
    from flask import send_from_directory
    @images.route('/<string:url>', methods=['GET'])
    # @jwt_required()
    def get_image(url):
        url = url.replace("#", "/")
        return send_from_directory('/app/images', url)