LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_SRC_FILES := sockev_cli.c
LOCAL_CFLAGS := -Wall -Werror

ifeq ($(TARGET_COMPILE_WITH_MSM_KERNEL),true)
LOCAL_HEADER_LIBRARIES := generated_kernel_headers
endif

LOCAL_CLANG := true
LOCAL_MODULE := sockev
LOCAL_MODULE_TAGS := optional

include $(BUILD_EXECUTABLE)
