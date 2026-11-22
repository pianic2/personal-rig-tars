# rig_omni dependency inventory — RTARS-15

Source is the upstream `main/idf_component.yml` at commit `c2b42cd73ef65f5cd2a158d6949f0273869454dc`.

**55 direct dependency declarations**, some conditioned on the target. The authoritative exact constraints and conditional rules are preserved at:
https://github.com/LuwuDynamics/rig_omni/blob/c2b42cd73ef65f5cd2a158d6949f0273869454dc/main/idf_component.yml

Direct component names:

```text
waveshare/esp_lcd_sh8601
espressif/esp_lcd_co5300
espressif/esp_lcd_ili9341
espressif/esp_lcd_gc9a01
espressif/esp_lcd_st77916
espressif/esp_lcd_axs15231b
espressif/esp_lcd_st7701
espressif/esp_lcd_st7796
espressif/esp_lcd_spd2010
espressif/esp_io_expander_tca9554
waveshare/custom_io_expander_ch32v003
espressif/esp_lcd_panel_io_additions
78/esp_lcd_nv3023
78/esp-wifi-connect
espressif/esp_audio_effects
espressif/esp_audio_codec
78/esp-ml307
78/uart-eth-modem
espressif/led_strip
espressif/esp_codec_dev
espressif/esp-sr
espressif/button
espressif/knob
espressif/esp32-camera
espressif/esp_video
espressif/esp_image_effects
espressif/esp_lcd_touch_ft5x06
espressif/esp_lcd_touch_gt911
espressif/esp_lcd_touch_gt1151
waveshare/esp_lcd_touch_cst9217
espressif/esp_lcd_touch_cst816s
lvgl/lvgl
esp_lvgl_port
espressif/esp_io_expander_tca95xx_16bit
espressif2022/image_player
78/xiaozhi-fonts
espressif2022/esp_emote_expression
espressif/adc_mic
espressif/esp_mmap_assets
espressif/adc_battery_estimation
espressif/esp_new_jpeg
wvirgil123/sscma_client
tny-robotics/sh1106-esp-idf
espressif/esp_lcd_jd9365
waveshare/esp_lcd_st7703
espressif/esp32_p4_function_ev_board
espressif/esp_lcd_ili9881c
espressif/esp_lcd_ek79007
espressif/esp_hosted
espressif/esp_wifi_remote
espfriends/servo_dog_ctrl
llgok/cpp_bus_driver
espressif/bmi270_sensor
espressif/esp_lcd_touch_st7123
espressif/iot_usbh_rndis
```

ESP-IDF requirement: `>=5.5.2`; observed toolchain: `5.5.3` (**declared compatibility PASS**).

**Reproducibility limitation:** no dependency lock was supplied; actual selected versions and transitive graph remain unverified. Pinning the Git commit alone is not a fully hermetic dependency lock.
