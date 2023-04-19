import unreal

desired_prefix = "T_skinType0d000_" 
assets_folder = "/Game/MetaHumans/Set_001/Body"

asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
assets = asset_registry.get_assets_by_path(assets_folder, recursive=False)

for asset in assets:
    print(asset)
    old_name = str(asset.asset_name)
    new_name = desired_prefix + old_name
    source_path = str(asset.package_name)
    destination_path = source_path.replace(old_name, new_name)
    unreal.EditorAssetLibrary.rename_asset(source_path, destination_path)