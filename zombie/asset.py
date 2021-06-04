class AssetManager:
    __assets={}
    @staticmethod
    def load_asset(asset_list_file="asset.z"):
        file=open(asset_list_file)
        data=file.read()
        file.close()
        data=data.split('\n')
        for asset in data:
            AssetManager.__assets.update({asset.split('=',1)[0].strip():asset.split('=',1)[1].strip()})
    @staticmethod
    def get_asset(_asset_name):
        return AssetManager.__assets[_asset_name]