import unreal

listnumber = "055"
skintype_name = "0d973"
desired_prefix = "T_" + "skinType" + skintype_name + "_"
source_folder = "/Game/MetaHumans/Set_" + listnumber +"/Face"
destination_folder = "/Game/YourDestinationFolderPath/skinType_" + skintype_name

asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
assets = asset_registry.get_assets_by_path(source_folder, recursive=False)

if not unreal.EditorAssetLibrary.does_directory_exist(destination_folder):
    unreal.EditorAssetLibrary.make_directory(destination_folder)

for asset in assets:
    old_name = str(asset.asset_name)
    new_name = desired_prefix + old_name

    source_path = str(asset.package_name)

    destination_path = source_path.replace(old_name, new_name)

    subdirectory_path = str(asset.package_path).replace(source_folder, "")
    destination_path = destination_folder + subdirectory_path + "/" + new_name

    unreal.EditorAssetLibrary.duplicate_asset(source_path, destination_path)
