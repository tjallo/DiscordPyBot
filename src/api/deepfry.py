from requests import get
from PIL import Image
from io import BytesIO
import deeppyer
from os.path import exists, abspath, curdir
from os import makedirs, listdir
from pathlib import Path



class DeepfryAPI:
    def __init__(self) -> None:
        data_folder = Path(abspath(curdir))
        self.temp_folder = data_folder / "temp"
        self.n_files = 0

        if not exists(self.temp_folder):
            makedirs(self.temp_folder)
        else:
            self.n_files = len(listdir(self.temp_folder))

        

    async def deepfry(self, image_url) -> Path:
        res = get(image_url)
        img = Image.open(BytesIO(res.content))
        result = await deeppyer.deepfry(img, flares=False)
        save_path = self.temp_folder / f"{self.n_files + 1}.jpg"
        result.save(save_path)

        return save_path