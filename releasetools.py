# Copyright (C) 2016 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def FullOTA_InstallEnd(info):
  info.script.AppendExtra('ifelse(is_mounted("/system"), unmount("/system"));')
  info.script.AppendExtra('ifelse(is_mounted("/vendor"), unmount("/vendor"));')
  info.script.AppendExtra('mount("ext4", "EMMC", "/dev/block/bootdevice/by-name/system", "/system");');
  info.script.AppendExtra('mount("ext4", "EMMC", "/dev/block/bootdevice/by-name/cache", "/vendor", "");')
  info.script.AppendExtra('mount("ext4", "EMMC", "/dev/block/bootdevice/by-name/modem", "/firmware", "");')
  info.script.AppendExtra('ui_print("Extracting modem firmware");')
  info.script.AppendExtra('run_program("/sbin/sh", "/vendor/bin/extract_firmware.sh");')
  info.script.AppendExtra('ui_print("Firmware extracted");')
  info.script.AppendExtra('ui_print("Wrapping shims");')
  info.script.AppendExtra('run_program("/sbin/sh", "/vendor/bin/wrap_shims.sh");')
  info.script.AppendExtra('ui_print("Shims wrapped");')
  info.script.AppendExtra('ui_print("Updating build props");')
  info.script.AppendExtra('run_program("/sbin/sh", "/vendor/bin/update_build_prop.sh");')
  info.script.AppendExtra('ui_print("Build props updated");')
  info.script.AppendExtra('unmount("/system");')
  info.script.AppendExtra('unmount("/vendor");')
  info.script.AppendExtra('unmount("/firmware");')

