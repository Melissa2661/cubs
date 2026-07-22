bl_info = {
    "name": "Auto-Fix USD Import FPS",
    "author": "W. M. Carbonneau",
    "version": (1, 0),
    "blender": (4, 2, 2),
    "location": "File > Import > Universal Scene Description (.usd*)",
    "description": "Automatically sets Blender scene FPS to match the imported USD* file's frame rate metadata.",
    "category": "Import-Export",
}
import bpy

class MyUSDImportHook(bpy.types.USDHook):
    bl_idname = "GetOffMyLawn.usd_import_hook"
    bl_label = "Custom USD Import Handler"

    @staticmethod
    def on_import(import_context):
        """Called after the USD stage is imported."""
        stage = import_context.get_stage()
        # You can read metadata from the stage here, 
        # such as extracting timeCodesPerSecond or custom properties
        
        # Example: Automatically fix the scene frame rate post-import
        # (Grabbing frame rate metadata from stage if available)
        fps = stage.GetTimeCodesPerSecond()
        if fps:
            bpy.context.scene.render.fps = int(fps)
            
        return True

def register():
    bpy.utils.register_class(MyUSDImportHook)

def unregister():
    bpy.utils.unregister_class(MyUSDImportHook)

if __name__ == "__main__":
    register()