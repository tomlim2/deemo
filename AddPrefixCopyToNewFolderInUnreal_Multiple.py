import unreal

skintype_values = {
    "001":"0d000",
    "002":"0d010",
    "003":"0d028",
    "004":"0d046",
    "005":"0d065",
    "006":"0d083",
    "007":"0d100",
    "008":"0d118",
    "009":"0d136",
    "010":"0d155",
    "011":"0d173",
    "012":"0d191",
    "013":"0d210",
    "014":"0d228",
    "015":"0d246",
    "016":"0d265",
    "017":"0d283",
    "018":"0d300",
    "019":"0d318",
    "020":"0d336",
    "021":"0d355",
    "022":"0d373",
    "023":"0d391",
    "024":"0d410",
    "025":"0d428",
    "026":"0d446",
    "027":"0d465",
    "028":"0d483",
    "029":"0d500",
    "030":"0d518",
    "031":"0d536",
    "032":"0d555",
    "033":"0d573",
    "034":"0d591",
    "035":"0d610",
    "036":"0d628",
    "037":"0d646",
    "038":"0d665",
    "039":"0d683",
    "040":"0d700",
    "041":"0d718",
    "042":"0d736",
    "043":"0d755",
    "044":"0d773",
    "045":"0d791",
    "046":"0d810",
    "047":"0d828",
    "048":"0d846",
    "049":"0d865",
    "050":"0d881",
    "051":"0d900",
    "052":"0d918",
    "053":"0d936",
    "054":"0d955",
    "055":"0d973",
    "056":"0d991",
}

asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()

for listnumber, skintype_name in skintype_values.items():
    source_folder = "/Game/MetaHumans/Set_" + listnumber + "/Face"
    desired_prefix = "T_" + "skinType" + skintype_name + "_"
    destination_folder = "/Game/SkinTypes/skinType_" + skintype_name

    assets = asset_registry.get_assets_by_path(source_folder, recursive=False)

    if not unreal.EditorAssetLibrary.does_directory_exist(destination_folder):
        unreal.EditorAssetLibrary.make_directory(destination_folder)

    for asset in assets:
        print(f"Asset: {asset.asset_name}, Class: {asset.asset_class_path}")
        if asset.asset_class_path.asset_name == "Texture2D":
            old_name = str(asset.asset_name)
            old_name_without_prefix = old_name.replace("T_", "", 1)
            new_name = desired_prefix + old_name_without_prefix

            source_path = str(asset.package_name)
            destination_path = source_path.replace(old_name, new_name)

            subdirectory_path = str(asset.package_path).replace(source_folder, "")
            destination_path = destination_folder + subdirectory_path + "/" + new_name

            unreal.EditorAssetLibrary.duplicate_asset(source_path, destination_path)
