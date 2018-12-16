LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := librmnetctl_headers
LOCAL_EXPORT_C_INCLUDE_DIRS:=$(LOCAL_PATH)/inc
include $(BUILD_HEADER_LIBRARY)

include $(CLEAR_VARS)
LOCAL_SRC_FILES := librmnetctl.c
LOCAL_CFLAGS := -Wall -Werror

LOCAL_C_INCLUDES := $(LOCAL_PATH)/inc
LOCAL_C_INCLUDES += $(LOCAL_PATH)
#ifeq ($(TARGET_COMPILE_WITH_MSM_KERNEL),true)
LOCAL_HEADER_LIBRARIES := generated_kernel_headers
#endif

LOCAL_CLANG := true
LOCAL_MODULE := librmnetctl
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_OWNER := qcom
LOCAL_VENDOR_MODULE := true
LOCAL_PROPRIETARY_MODULE := true

include $(BUILD_SHARED_LIBRARY)
