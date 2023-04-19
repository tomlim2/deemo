import unreal

listnumber = "055"
source_folder = "/Game/MetaHumans/Set_" + listnumber + "/Face"

skintype_values = [
    "0d000",
    "0d010",
    "0d028",
    "0d046",
    "0d065",
    "0d083",
    "0d100",
    "0d118",
    "0d136",
    "0d155",
    "0d173",
    "0d191",
    "0d210",
    "0d228",
    "0d246",
    "0d265",
    "0d283",
    "0d300",
    "0d318",
    "0d336",
    "0d355",
    "0d373",
    "0d391",
    "0d410",
    "0d428",
    "0d446",
    "0d465",
    "0d483",
    "0d500",
    "0d518",
    "0d536",
    "0d555",
    "0d573",
    "0d591",
    "0d610",
    "0d628",
    "0d646",
    "0d665",
    "0d683",
    "0d700",
    "0d718",
    "0d736",
    "0d755",
    "0d773",
    "0d791",
    "0d810",
    "0d828",
    "0d846",
    "0d865",
    "0d881",
    "0d900",
    "0d918",
    "0d936",
    "0d955",
    "0d973",
    "0d991",
]


skintype_name = "0d973"
desired_prefix = "T_" + "skinType" + skintype_name + "_"
destination_folder = "/Game/YourDestinationFolderPath/skinType_" + skintype_name

asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
assets = asset_registry.get_assets_by_path(source_folder, recursive=False)

if not unreal.EditorAssetLibrary.does_directory_exist(destination_folder):
    unreal.EditorAssetLibrary.make_directory(destination_folder)

for asset in assets:
    old_name = str(asset.asset_name)
    # Remove the "T_" prefix from the old name
    old_name_without_prefix = old_name.replace("T_", "", 1)
    # Add the desired prefix to the new name
    new_name = desired_prefix + old_name_without_prefix

    source_path = str(asset.package_name)

    destination_path = source_path.replace(old_name, new_name)

    subdirectory_path = str(asset.package_path).replace(source_folder, "")
    destination_path = destination_folder + subdirectory_path + "/" + new_name

    unreal.EditorAssetLibrary.duplicate_asset(source_path, destination_path)
