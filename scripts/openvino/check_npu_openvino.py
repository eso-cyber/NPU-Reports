import openvino.runtime as ov

core = ov.Core()
devices = core.available_devices

print("🔎 Checking OpenVINO Runtime...")
for device in devices:
    device_name = core.get_property(device, "FULL_DEVICE_NAME")
    print(f"✅ Found Device: {device} ({device_name})")

if "NPU" in devices:
    print("\n🚀 SUCCESS: Intel NPU is ready for OpenVINO inference!")
else:
    print("\n⚠️ WARNING: NPU not detected by OpenVINO. Check drivers.")
