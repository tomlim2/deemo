import unreal

folder_path = "/Game/Content/metahumanAssets/Set_001/Face/"
old_prefix = "Face"
new_prefix = "hi"

asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
asset_data_list = asset_registry.get_assets_by_path(folder_path, recursive=True)

for asset_data in asset_data_list:
    asset_name = asset_data.asset_name
    if asset_name.startswith(old_prefix):
        new_asset_name = new_prefix + asset_name[len(old_prefix):]
        old_asset_path = asset_data.object_path
        new_asset_path = folder_path + new_asset_name

        rename_result = unreal.EditorAssetLibrary.rename_asset(old_asset_path, new_asset_path)
        if not rename_result:
            unreal.log_warning("Failed to rename '{}' to '{}'.".format(old_asset_path, new_asset_path))
        else:
            unreal.log("Renamed '{}' to '{}'.".format(old_asset_path, new_asset_path))