import os
import subprocess
import urllib.request
import winreg
import sys
import requests
import shutil
import json
from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QLabel, QRadioButton
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget,
                             QVBoxLayout, QCheckBox, QLabel, QPushButton)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QRadioButton, QButtonGroup
from PyQt5.QtGui import QFont 
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # メインウィンドウのプロパティを設定します
        self.setWindowTitle('PyQt5 Tab Example')
        self.setGeometry(100, 30, 1280, 960)
        self.setStyleSheet("background-color: white;")

        # タブウィジェットを作成します
        tab_widget = QTabWidget(self)
        tab_widget.setGeometry(20, 20, 1240, 920)  # タブウィジェットの位置とサイズを設定します

        # タブを作成します
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        # タブのタイトルを設定します
        tab_widget.addTab(self.tab1, "モデルダウンロードとコントロールネット(forge)")
        tab_widget.addTab(self.tab2, "拡張機能(forge)")
        tab_widget.addTab(self.tab3, "1111版 AUTOMATIC)")
        tab_widget.addTab(self.tab4, "ComfyUI")
        tab_widget.addTab(self.tab5, "全体設定")

        # タブ1のレイアウトを設定します
        self.tab1_layout = QVBoxLayout(self.tab1)
        self.tab1.setLayout(self.tab1_layout)
        # タブ2のレイアウトを設定します
        self.tab2_layout = QVBoxLayout(self.tab2)
        self.tab2.setLayout(self.tab2_layout)
        # タブ3のレイアウトを設定します
        self.tab3_layout = QVBoxLayout(self.tab3)
        self.tab3.setLayout(self.tab3_layout)
        # タブ3のレイアウトを設定します
        self.tab4_layout = QVBoxLayout(self.tab3)
        self.tab4.setLayout(self.tab3_layout)
        # タブ3のレイアウトを設定します
        self.tab5_layout = QVBoxLayout(self.tab3)
        self.tab5.setLayout(self.tab3_layout)

        # checkpointのフォルダのパス
        os.chdir('..')
        folder_path = 'stable-diffusion-webui-forge/models/Stable-diffusion'
        # 確認したい特定の文字列
        specific_string0 = 'hanamomopony_v14'
        specific_string1 = 'momoiropony'
        specific_string2 = 'animagine-xl-3.1'
        specific_string3 = 'fuduki_mix'
        specific_string4 = 'Juggernaut-XL'

        # チェックボックスの初期ラベル
        checkbox0_label = "hanamomopony_v14(6.46GB)"
        checkbox1_label = "momoiropony_v1.4(6.46GB)"
        checkbox2_label = "animagine-xl-3.1(6.46GB)"
        checkbox3_label = "fuduki_mix_v2(6.46GB)"
        checkbox4_label = "Juggernaut-XL_v9(7.11GB)"

        # フォルダが存在し、かつディレクトリであることを確認
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            # フォルダ内のファイル名を取得
            files = os.listdir(folder_path)

            # 各ファイルについて特定の文字列が含まれているか確認し、ラベルを更新
            file_contains_string = any(specific_string0 in file for file in files)
            checkbox0_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string1 in file for file in files)
            checkbox1_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string2 in file for file in files)
            checkbox2_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string3 in file for file in files)
            checkbox3_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string4 in file for file in files)
            checkbox4_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"

        else:
            print(f"指定されたフォルダー {folder_path} は存在しません。")
            checkbox0_label += " ×ダウンロードされていません"
            checkbox1_label += " ×ダウンロードされていません"
            checkbox2_label += " ×ダウンロードされていません"
            checkbox3_label += " ×ダウンロードされていません"
            checkbox4_label += " ×ダウンロードされていません"

        # ControlNetのフォルダのパス
        folder_path = 'stable-diffusion-webui-forge/models/ControlNet'

        # 確認したい特定の文字列
        specific_string0 = 'canny'
        specific_string1 = 'depth'
        specific_string2 = 'openpose'
        specific_string3 = 'softedge'

        # チェックボックスの初期ラベル
        canny_label = "canny"
        depth_label = "depth"
        openpose_label = "openpose"
        softedge_label = "softedge"

        # フォルダが存在し、かつディレクトリであることを確認
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            # フォルダ内のファイル名を取得
            files = os.listdir(folder_path)

            # 各ファイルについて特定の文字列が含まれているか確認し、ラベルを更新
            file_contains_string = any(specific_string0 in file for file in files)
            canny_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string1 in file for file in files)
            depth_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string2 in file for file in files)
            openpose_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string3 in file for file in files)
            softedge_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"

        else:
            print(f"指定されたフォルダー {folder_path} は存在しません。")
            canny_label += " ×ダウンロードされていません"
            depth_label += " ×ダウンロードされていません"
            openpose_label += " ×ダウンロードされていません"
            softedge_label += " ×ダウンロードされていません"

        # 文字スタイルの設定値を変数に格納
        tatle_style = "font-size: 18px; font-weight: bold;"
        label_style = "font-size: 16px;"

        # ベースのY座標とチェックボックス間の間隔を設定
        base_y = 80
        spacing = 35

        # タブ1のタイトルラベルを作成します
        self.title_label = QLabel("stableDiffusion webUI forge版インストール", self.tab1)
        self.title_label.setGeometry(30, base_y - (spacing * 1), 450, 30)
        self.title_label.setStyleSheet("font-size: 24px;")

        # タイトルラベルを作成します
        self.title_label = QLabel("ダウンロードするモデルを選択", self.tab1)
        self.title_label.setGeometry(50, base_y + (spacing * 0), 400, 30)  # ラベルの位置とサイズを設定します
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        # hanamomopony_v14
        self.checkbox0 = QCheckBox(checkbox0_label, self.tab1)
        self.checkbox0.setGeometry(50, base_y + (spacing * 1), 400, 30)
        self.checkbox0.setStyleSheet(label_style)
        self.checkbox0.stateChanged.connect(lambda: self.on_checkbox_toggled(self.checkbox0))

        # momoiropony_v14
        self.checkbox1 = QCheckBox(checkbox1_label, self.tab1)
        self.checkbox1.setGeometry(50, base_y + (spacing * 2), 400, 30)
        self.checkbox1.setStyleSheet(label_style)
        self.checkbox1.stateChanged.connect(lambda: self.on_checkbox_toggled(self.checkbox1))
        
        # animagine-xl-3.1
        self.checkbox2 = QCheckBox(checkbox2_label, self.tab1)
        self.checkbox2.setGeometry(50, base_y + (spacing * 3), 400, 30)
        self.checkbox2.setStyleSheet(label_style)
        self.checkbox2.stateChanged.connect(lambda: self.on_checkbox_toggled(self.checkbox2))
        
        # fuduki_mix_v2
        self.checkbox3 = QCheckBox(checkbox3_label, self.tab1)
        self.checkbox3.setGeometry(50, base_y + (spacing * 4), 400, 30)
        self.checkbox3.setStyleSheet(label_style)
        self.checkbox3.stateChanged.connect(lambda: self.on_checkbox_toggled(self.checkbox3))
        
        # Juggernaut-XL_v9
        self.checkbox4 = QCheckBox(checkbox4_label, self.tab1)
        self.checkbox4.setGeometry(50, base_y + (spacing * 5), 400, 30)
        self.checkbox4.setStyleSheet(label_style)
        self.checkbox4.stateChanged.connect(lambda: self.on_checkbox_toggled(self.checkbox4))

        # タイトルラベルを作成します
        self.title_label = QLabel("ダウンロードするコントロールネットを選択してください", self.tab1)
        self.title_label.setGeometry(50, base_y + (spacing * 7), 450, 30)  # ラベルの位置とサイズを設定します
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        # "canny" チェックボックス
        self.checkbox_canny = QCheckBox(canny_label, self.tab1)
        self.checkbox_canny.setGeometry(50, base_y + (spacing * 8), 400, 30)
        self.checkbox_canny.setStyleSheet(label_style)
        self.checkbox_canny.stateChanged.connect(lambda: self.on_checkbox_toggled(self.checkbox_canny))

        # "depth" チェックボックス
        self.checkbox_depth = QCheckBox(depth_label, self.tab1)
        self.checkbox_depth.setGeometry(50, base_y + (spacing * 9), 400, 30)
        self.checkbox_depth.setStyleSheet(label_style)
        self.checkbox_depth.stateChanged.connect(lambda: self.on_checkbox_toggled(self.checkbox_depth))

        # "openpose"
        self.checkbox_openpose = QCheckBox(openpose_label, self.tab1)
        self.checkbox_openpose.setGeometry(50, base_y + (spacing * 10), 400, 30)
        self.checkbox_openpose.setStyleSheet(label_style)
        self.checkbox_openpose.stateChanged.connect(lambda: self.on_checkbox_toggled(self.checkbox_openpose))
        
        # "softedge"
        self.checkbox_softedge = QCheckBox(softedge_label, self.tab1)
        self.checkbox_softedge.setGeometry(50, base_y + (spacing * 11), 400, 30)
        self.checkbox_softedge.setStyleSheet(label_style)
        self.checkbox_softedge.stateChanged.connect(lambda: self.on_checkbox_toggled(self.checkbox_softedge))

# ここからタブ2
        # 確認したい特定の文字列
        specific_string0 = 'localization-ja_JP'
        specific_string1 = 'tagcomplete'
        specific_string2 = 'history-slider'
        specific_string3 = 'ar-plus'
        specific_string4 = 'Config-Presets'
        specific_string5 = 'adetailer'
        specific_string6 = 'lama_cleaner'
        specific_string7 = 'openpose-editor'
        specific_string8 = 'dynamic-prompts'
        specific_string9 = 'lora-block-weight'
        specific_string10 = 'supermerger'
        
        localization_label = "日本語化"
        tagcomplete_label  = "予測変換機能"
        history_label = "プロンプト履歴"
        ar_label = "縦横比変更"
        Presets_label = "設定保存"
        adetailer_label = "顔検出品質向上"
        lama_label = "部分消去"
        pose_label = "姿勢素体編集"
        dynamic_label = "ランダムプロンプト"
        weight_label = "LoRA部分適用"
        supermerger_label = "モデル合成"

        # extensionsのフォルダのパス
        folder_path = 'stable-diffusion-webui-forge/extensions'
        # フォルダが存在し、かつディレクトリであることを確認
        if os.path.exists(folder_path) and os.path.isdir(folder_path):

            # フォルダ内のファイル名を取得
            files = os.listdir(folder_path)

            # 各ファイルについて特定の文字列が含まれているか確認し、ラベルを更新
            file_contains_string = any(specific_string0 in file for file in files)
            localization_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string1 in file for file in files)
            tagcomplete_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string2 in file for file in files)
            history_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string3 in file for file in files)
            ar_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string4 in file for file in files)
            Presets_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string5 in file for file in files)
            adetailer_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string6 in file for file in files)
            lama_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string7 in file for file in files)
            pose_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string8 in file for file in files)
            dynamic_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string9 in file for file in files)
            weight_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string10 in file for file in files)
            supermerger_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
        else:
            print(f"指定されたフォルダー {folder_path} は存在しません。")
            localization_label += " ×ダウンロードされていません"
            tagcomplete_label += " ×ダウンロードされていません"
            history_label += " ×ダウンロードされていません"
            ar_label += " ×ダウンロードされていません"
            Presets_label += " ×ダウンロードされていません"
            adetailer_label += " ×ダウンロードされていません"
            lama_label += " ×ダウンロードされていません"
            pose_label += " ×ダウンロードされていません"
            dynamic_label += " ×ダウンロードされていません"
            weight_label += " ×ダウンロードされていません"
            supermerger_label += " ×ダウンロードされていません"

        # タイトルラベルを作成します
        self.title_label = QLabel("ダウンロードする基本拡張機能を選択してください", self.tab2)
        self.title_label.setGeometry(50, base_y - (spacing * 1), 400, 30)  # ラベルの位置とサイズを設定します
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        
         # "localization" チェックボックス
        self.checkbox_localization = QCheckBox(localization_label, self.tab2)
        self.checkbox_localization.setGeometry(50, base_y + (spacing * 0), 400, 30)
        self.checkbox_localization.setStyleSheet("font-size: 18px; spacing: 20px;")
        self.checkbox_localization.toggled.connect(lambda checked: self.on_checkbox_toggled_tab2(self.checkbox_localization))
        
        # "tagcomplete" チェックボックス
        self.checkbox_tagcomplete = QCheckBox(tagcomplete_label, self.tab2)
        self.checkbox_tagcomplete.setGeometry(50, base_y + (spacing * 1), 400, 30)
        self.checkbox_tagcomplete.setStyleSheet("font-size: 18px; spacing: 20px;")
        self.checkbox_tagcomplete.toggled.connect(lambda checked: self.on_checkbox_toggled_tab2(self.checkbox_tagcomplete))
        
        # "history-slider" チェックボックス
        self.checkbox_history = QCheckBox(history_label, self.tab2)
        self.checkbox_history.setGeometry(50, base_y + (spacing * 2), 400, 30)
        self.checkbox_history.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_history.toggled.connect(lambda checked: self.on_checkbox_toggled_tab2(self.checkbox_history))

        # "ar-plus"
        self.checkbox_ar = QCheckBox(ar_label, self.tab2)
        self.checkbox_ar.setGeometry(50, base_y + (spacing * 3), 400, 30)
        self.checkbox_ar.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_ar.toggled.connect(lambda checked: self.on_checkbox_toggled_tab2(self.checkbox_ar))

        # "Presets"
        self.checkbox_Presets = QCheckBox(Presets_label, self.tab2)
        self.checkbox_Presets.setGeometry(50, base_y + (spacing * 4), 400, 30)
        self.checkbox_Presets.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_Presets.toggled.connect(lambda checked: self.on_checkbox_toggled_tab2(self.checkbox_Presets))

        # "adetailer"
        self.checkbox_adetailer = QCheckBox(adetailer_label, self.tab2)
        self.checkbox_adetailer.setGeometry(50, base_y + (spacing * 5), 400, 30)
        self.checkbox_adetailer.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_adetailer.toggled.connect(lambda checked: self.on_checkbox_toggled_tab2(self.checkbox_adetailer))

        # "lama"
        self.checkbox_lama = QCheckBox(lama_label, self.tab2)
        self.checkbox_lama.setGeometry(50, base_y + (spacing * 6), 400, 30)
        self.checkbox_lama.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_lama.toggled.connect(lambda checked: self.on_checkbox_toggled_tab2(self.checkbox_lama))

        # "openpose-editor"
        self.checkbox_pose = QCheckBox(pose_label, self.tab2)
        self.checkbox_pose.setGeometry(50, base_y + (spacing * 7), 400, 30)
        self.checkbox_pose.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_pose.toggled.connect(lambda checked: self.on_checkbox_toggled_tab2(self.checkbox_pose))

        # "dynamic-prompts"
        self.checkbox_dynamic = QCheckBox(dynamic_label, self.tab2)
        self.checkbox_dynamic.setGeometry(50, base_y + (spacing * 8), 400, 30)
        self.checkbox_dynamic.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_dynamic.toggled.connect(lambda checked: self.on_checkbox_toggled_tab2(self.checkbox_dynamic))

        # タイトルラベルを作成します
        self.title_label = QLabel("高度拡張機能", self.tab2)
        self.title_label.setGeometry(50, base_y + (spacing * 10), 400, 30)  # ラベルの位置とサイズを設定します
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        # "lora-block-weight"
        self.checkbox_weight = QCheckBox(weight_label, self.tab2)
        self.checkbox_weight.setGeometry(50, base_y + (spacing * 11), 400, 30)
        self.checkbox_weight.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_weight.toggled.connect(lambda checked: self.on_checkbox_toggled_tab2(self.checkbox_weight))

        # "supermerger"
        self.checkbox_supermerger = QCheckBox(supermerger_label, self.tab2)
        self.checkbox_supermerger.setGeometry(50, base_y + (spacing * 12), 400, 30)
        self.checkbox_supermerger.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_supermerger.toggled.connect(lambda checked: self.on_checkbox_toggled_tab2(self.checkbox_supermerger))

        # tab1用のダウンロードボタンを作成します
        download_tab1_button = QPushButton("インストールを開始", self.tab1)
        download_tab1_button.setGeometry(50, base_y + (spacing * 15), 200, 40)
        download_tab1_button.setStyleSheet("background-color: #00ba7c; color: white; font-size: 16px;")

        # tab1用の起動ボタンを作成します
        launch_tab1_button = QPushButton("起動", self.tab1)
        launch_tab1_button.setGeometry(255, base_y + (spacing * 15), 200, 40)
        launch_tab1_button.setStyleSheet("background-color: #f91880; color: white; font-size: 16px; ")

        # tab1用の更新用を作成します
        git_pull_forge_tab1_button = QPushButton("更新", self.tab1)
        git_pull_forge_tab1_button.setGeometry(50, base_y + (spacing * 16) + 25, 200, 40)
        git_pull_forge_tab1_button.setStyleSheet("background-color: #1d9bf0; color: white; font-size: 16px; ")

        # tab2用のダウンロードボタンを作成します
        download_tab2_button = QPushButton("インストールを開始", self.tab2)
        download_tab2_button.setGeometry(50, base_y + (spacing * 15), 200, 40)
        download_tab2_button.setStyleSheet("background-color: #00ba7c; color: white; font-size: 16px;")

        # tab2用の起動ボタンを作成します
        launch_tab2_button = QPushButton("起動", self.tab2)
        launch_tab2_button.setGeometry(255, base_y + (spacing * 15), 200, 40)
        launch_tab2_button.setStyleSheet("background-color: #f91880; color: white; font-size: 16px;")

        # tab2用の更新ボタンを作成します
        git_pull_forge_tab2_button = QPushButton("更新", self.tab2)
        git_pull_forge_tab2_button.setGeometry(50, base_y + (spacing * 16) + 25, 200, 40)
        git_pull_forge_tab2_button.setStyleSheet("background-color: #1d9bf0; color: white; font-size: 16px; ")

        # tab1用のクリックイベントを接続します
        download_tab1_button.clicked.connect(self.start_download)
        launch_tab1_button.clicked.connect(self.launch_webui)
        git_pull_forge_tab1_button.clicked.connect(self.git_pull_forge)

        # tab2用のクリックイベントを接続します
        download_tab2_button.clicked.connect(self.start_download)
        launch_tab2_button.clicked.connect(self.launch_webui)
        git_pull_forge_tab2_button.clicked.connect(self.git_pull_forge)

# ここからタブ3
        tab3base_y = 20
        spacing = 35
        # タイトルラベルを作成します
        self.title_label = QLabel("stableDiffusion WebUI 1111版　インストール", self.tab3)
        self.title_label.setGeometry(50, tab3base_y, 400, 30)  # ラベルの位置とサイズを設定します
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        
         # ラジオボタンを作成します
        self.radio_button1 = QRadioButton("Forge版とモデルを共有する", self.tab3)
        self.radio_button1.setGeometry(50, tab3base_y + (spacing * 1), 300, 30)
        self.radio_button1.setStyleSheet("font-size: 18px;")
        self.radio_button2 = QRadioButton("Forge版とモデルを共有しない", self.tab3)
        self.radio_button2.setGeometry(50, tab3base_y + (spacing * 2), 300, 30)
        self.radio_button2.setStyleSheet("font-size: 18px;")
        self.radio_button1.setChecked(True) # デフォルトで選択状態にします
        # ラジオボタンをグループ化します
        self.radio_button_group = QButtonGroup(self.tab3)
        self.radio_button_group.addButton(self.radio_button1)
        self.radio_button_group.addButton(self.radio_button2)

        # 確認したい特定の文字列
        specific_string0 = 'localization-ja_JP'
        specific_string1 = 'tagcomplete'
        specific_string2 = 'history-slider'
        specific_string3 = 'ar-plus'
        specific_string4 = 'Config-Presets'
        specific_string5 = 'adetailer'
        specific_string6 = 'lama_cleaner'
        specific_string7 = 'openpose-editor'
        specific_string8 = 'dynamic-prompts'
        specific_string9 = 'lora-block-weight'
        specific_string10 = 'supermerger'
        specific_string11 = 'ControlNet'
        
        localization_label = "日本語化"
        tagcomplete_label  = "予測変換機能"
        history_label = "プロンプト履歴"
        ar_label = "縦横比変更"
        Presets_label = "設定保存"
        adetailer_label = "顔検出品質向上"
        lama_label = "部分消去"
        pose_label = "姿勢素体編集"
        dynamic_label = "ランダムプロンプト"
        weight_label = "LoRA部分適用"
        supermerger_label = "モデル合成"
        controlnet_label = 'コントロールネット'

        # ControlNetのフォルダのパス
        folder_path = 'stable-diffusion-webui/extensions'
        # フォルダが存在し、かつディレクトリであることを確認
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            # フォルダ内のファイル名を取得
            files = os.listdir(folder_path)

            # 各ファイルについて特定の文字列が含まれているか確認し、ラベルを更新
            file_contains_string = any(specific_string0 in file for file in files)
            localization_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string1 in file for file in files)
            tagcomplete_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string2 in file for file in files)
            history_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string3 in file for file in files)
            ar_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string4 in file for file in files)
            Presets_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string5 in file for file in files)
            adetailer_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string6 in file for file in files)
            lama_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string7 in file for file in files)
            pose_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string8 in file for file in files)
            dynamic_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string9 in file for file in files)
            weight_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string10 in file for file in files)
            supermerger_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
            file_contains_string = any(specific_string11 in file for file in files)
            controlnet_label += " 〇ダウンロード済" if file_contains_string else " ×ダウンロードされていません"
        else:
            print(f"指定されたフォルダー {folder_path} は存在しません。")
            localization_label += " ×ダウンロードされていません"
            tagcomplete_label += " ×ダウンロードされていません"
            history_label += " ×ダウンロードされていません"
            ar_label += " ×ダウンロードされていません"
            Presets_label += " ×ダウンロードされていません"
            adetailer_label += " ×ダウンロードされていません"
            lama_label += " ×ダウンロードされていません"
            pose_label += " ×ダウンロードされていません"
            dynamic_label += " ×ダウンロードされていません"
            weight_label += " ×ダウンロードされていません"
            supermerger_label += " ×ダウンロードされていません"
            controlnet_label += " ×ダウンロードされていません"

        # タイトルラベルを作成します
        self.title_label = QLabel("モデルを共有するか選択してください", self.tab3)
        self.title_label.setGeometry(50, tab3base_y - (spacing * 3), 400, 30)  # ラベルの位置とサイズを設定します
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        # サブタイトルを作成します
        self.title_label = QLabel("ダウンロードする基本拡張機能を選択してください", self.tab3)
        self.title_label.setGeometry(50, tab3base_y + (spacing * 3), 400, 30)  # ラベルの位置とサイズを設定します
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        # "controlnet" チェックボックス
        self.checkbox_controlnet1111 = QCheckBox(controlnet_label, self.tab3)
        self.checkbox_controlnet1111.setGeometry(50, tab3base_y + (spacing * 4), 400, 30)
        self.checkbox_controlnet1111.setStyleSheet("font-size: 18px; spacing: 20px;")
        self.checkbox_controlnet1111.toggled.connect(lambda checked: self.on_checkbox_toggled_tab3(self.checkbox_controlnet1111))

         # "localization" チェックボックス
        self.checkbox_localization1111 = QCheckBox(localization_label, self.tab3)
        self.checkbox_localization1111.setGeometry(50, tab3base_y + (spacing * 5), 400, 30)
        self.checkbox_localization1111.setStyleSheet("font-size: 18px; spacing: 20px;")
        self.checkbox_localization1111.toggled.connect(lambda checked: self.on_checkbox_toggled_tab3(self.checkbox_localization1111))
        
        # "tagcomplete" チェックボックス
        self.checkbox_tagcomplete1111 = QCheckBox(tagcomplete_label, self.tab3)
        self.checkbox_tagcomplete1111.setGeometry(50, tab3base_y + (spacing * 6), 400, 30)
        self.checkbox_tagcomplete1111.setStyleSheet("font-size: 18px; spacing: 20px;")
        self.checkbox_tagcomplete1111.toggled.connect(lambda checked: self.on_checkbox_toggled_tab3(self.checkbox_tagcomplete1111))
        
        # "history-slider" チェックボックス
        self.checkbox_history1111 = QCheckBox(history_label, self.tab3)
        self.checkbox_history1111.setGeometry(50, tab3base_y + (spacing * 7), 400, 30)
        self.checkbox_history1111.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_history1111.toggled.connect(lambda checked: self.on_checkbox_toggled_tab3(self.checkbox_history1111))

        # "ar-plus"
        self.checkbox_ar1111 = QCheckBox(ar_label, self.tab3)
        self.checkbox_ar1111.setGeometry(50, tab3base_y + (spacing * 8), 400, 30)
        self.checkbox_ar1111.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_ar1111.toggled.connect(lambda checked: self.on_checkbox_toggled_tab3(self.checkbox_ar1111))

        # "Presets"
        self.checkbox_Presets1111 = QCheckBox(Presets_label, self.tab3)
        self.checkbox_Presets1111.setGeometry(50, tab3base_y + (spacing * 9), 400, 30)
        self.checkbox_Presets1111.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_Presets1111.toggled.connect(lambda checked: self.on_checkbox_toggled_tab3(self.checkbox_Presets1111))

        # "adetailer"
        self.checkbox_adetailer1111 = QCheckBox(adetailer_label, self.tab3)
        self.checkbox_adetailer1111.setGeometry(50, tab3base_y + (spacing * 10), 400, 30)
        self.checkbox_adetailer1111.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_adetailer1111.toggled.connect(lambda checked: self.on_checkbox_toggled_tab3(self.checkbox_adetailer1111))

        # "lama"
        self.checkbox_lama1111 = QCheckBox(lama_label, self.tab3)
        self.checkbox_lama1111.setGeometry(50, tab3base_y + (spacing * 11), 400, 30)
        self.checkbox_lama1111.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_lama1111.toggled.connect(lambda checked: self.on_checkbox_toggled_tab3(self.checkbox_lama1111))

        # "openpose-editor"
        self.checkbox_pose1111 = QCheckBox(pose_label, self.tab3)
        self.checkbox_pose1111.setGeometry(50, tab3base_y + (spacing * 12), 400, 30)
        self.checkbox_pose1111.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_pose1111.toggled.connect(lambda checked: self.on_checkbox_toggled_tab3(self.checkbox_pose1111))

        # "dynamic-prompts"
        self.checkbox_dynamic1111 = QCheckBox(dynamic_label, self.tab3)
        self.checkbox_dynamic1111.setGeometry(50, tab3base_y + (spacing * 13), 400, 30)
        self.checkbox_dynamic1111.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_dynamic1111.toggled.connect(lambda checked: self.on_checkbox_toggled_tab3(self.checkbox_dynamic1111))

        # タイトルラベルを作成します
        self.title_label = QLabel("高度拡張機能", self.tab3)
        self.title_label.setGeometry(50, tab3base_y + (spacing * 14), 400, 30)  # ラベルの位置とサイズを設定します
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        # "lora-block-weight"
        self.checkbox_weight1111 = QCheckBox(weight_label, self.tab3)
        self.checkbox_weight1111.setGeometry(50, tab3base_y + (spacing * 15), 400, 30)
        self.checkbox_weight1111.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_weight1111.toggled.connect(lambda checked: self.on_checkbox_toggled_tab3(self.checkbox_weight1111))

        # "supermerger"
        self.checkbox_supermerger1111 = QCheckBox(supermerger_label, self.tab3)
        self.checkbox_supermerger1111.setGeometry(50, tab3base_y + (spacing * 16), 400, 30)
        self.checkbox_supermerger1111.setStyleSheet("font-size: 18px;spacing: 20px;")
        self.checkbox_supermerger1111.toggled.connect(lambda checked: self.on_checkbox_toggled_tab3(self.checkbox_supermerger1111))

        # tab3用のダウンロードボタンを作成します
        download_tab3_button = QPushButton("インストールを開始", self.tab3)
        download_tab3_button.setGeometry(50, base_y + (spacing * 17), 200, 40)
        download_tab3_button.setStyleSheet("background-color: #00ba7c; color: white; font-size: 16px;")

        # tab3用の起動ボタンを作成します
        launch_tab3_button = QPushButton("起動", self.tab3)
        launch_tab3_button.setGeometry(255, base_y + (spacing * 17), 200, 40)
        launch_tab3_button.setStyleSheet("background-color: #f91880; color: white; font-size: 16px;")

        # tab2用の更新ボタンを作成します
        git_pull_webui1111_tab3_button = QPushButton("更新", self.tab3)
        git_pull_webui1111_tab3_button.setGeometry(50, base_y + (spacing * 18) + 25, 200, 40)
        git_pull_webui1111_tab3_button.setStyleSheet("background-color: #1d9bf0; color: white; font-size: 16px; ")

        # tab3用のクリックイベントを接続します
        download_tab3_button.clicked.connect(self.start_download1111)
        launch_tab3_button.clicked.connect(self.launch_webui1111)
        git_pull_webui1111_tab3_button.clicked.connect(self.git_pull_webui1111)

# ここからタブ4
        tab4base_y = 20
        spacing = 35
        # タイトルラベルを作成します
        self.title_label = QLabel("ComfyUI", self.tab4)
        self.title_label.setGeometry(50, tab3base_y, 400, 30)  # ラベルの位置とサイズを設定します
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")

# ここからタブ5
        tab5base_y = 20
        spacing = 35
        # タイトルラベルを作成します
        self.title_label = QLabel("全体設定", self.tab5)
        self.title_label.setGeometry(50, tab3base_y, 400, 30)  # ラベルの位置とサイズを設定します
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")






# 画像の表示
        # image_labelの初期化
        self.image_label_tab1 = QLabel(self.tab1)
        self.image_label_tab1.setAlignment(Qt.AlignCenter)
        # 位置とサイズを設定（絶対位置を設定したい場合）
        self.image_label_tab1.move(496, 255)  # 位置とサイズを設定
        # tab1_layout.addWidget(self.image_label)  # レイアウト管理を使わない場合はこの行をコメントアウト
        
        # image_label_tab2の初期化
        self.image_label_tab2 = QLabel(self.tab2)
        self.image_label_tab2.setAlignment(Qt.AlignCenter)
        # 位置とサイズを設定（絶対位置を設定したい場合）
        self.image_label_tab2.move(496, 255)  # 位置とサイズを設定

        # image_label_tab3の初期化
        self.image_label_tab3 = QLabel(self.tab3)
        self.image_label_tab3.setAlignment(Qt.AlignCenter)
        # 位置とサイズを設定（絶対位置を設定したい場合）
        self.image_label_tab3.move(496, 255)  # 位置とサイズを設定

        # タブ1のテキストラベル初期化
        self.text_label_tab1 = QLabel(self.tab1)
        self.text_label_tab1.move(500, 0)
        self.text_label_tab1.setFixedWidth(700)
        self.text_label_tab1.setFixedHeight(200)
        self.text_label_tab1.setWordWrap(True)
        # タブ2のテキストラベル初期化
        self.text_label_tab2 = QLabel(self.tab2)
        self.text_label_tab2.move(500, 0)
        self.text_label_tab2.setFixedWidth(700)
        self.text_label_tab2.setFixedHeight(200)
        self.text_label_tab2.setWordWrap(True)
        # タブ3のテキストラベル初期化
        self.text_label_tab3 = QLabel(self.tab3)
        self.text_label_tab3.move(500, 0)
        self.text_label_tab3.setFixedWidth(700)
        self.text_label_tab3.setFixedHeight(200)
        self.text_label_tab3.setWordWrap(True)

        # スタイルシートを使用してフォントとサイズを設定
        self.text_label_tab1.setStyleSheet("QLabel { font-family: 'Yu Gothic'; font-size: 18px; }")
        self.text_label_tab2.setStyleSheet("QLabel { font-family: 'Yu Gothic'; font-size: 18px; }")
        self.text_label_tab3.setStyleSheet("QLabel { font-family: 'Yu Gothic'; font-size: 18px; }")
        # 最後にアクティブだったチェックボックスに基づいて画像を更新
    def on_checkbox_toggled(self, sender):
        if sender.isChecked():
            if sender == self.checkbox0:
                pixmap = QPixmap('code/image/model0.png')
                self.text_label_tab1.setText("hanamomopony_v14\n　momoiroponyの作者が新たに出しているシリーズ。momoiroponyに比べて絵柄に幅を持たせたモデルと思われます。momoiroponyの特徴と大きく変わりなく絵柄が安定しており、手の正確な描写や難しいアングル・R18系の画像を出力するのに向いています。") 
                self.text_label_tab1.setStyleSheet("QLabel { font-family: 'Yu Gothic'; font-size: 16px; }")
            elif sender == self.checkbox1:
                pixmap = QPixmap('code/image/model1.png')
                self.text_label_tab1.setText("momoiropony_V1.4\n　momoiroponyはイラストモデルの中でも最高峰の性能を持っています。絵柄が安定しており、手の正確な描写や難しいアングル・R18系の画像を出力するのに向いています。") 
                self.text_label_tab1.setStyleSheet("QLabel { font-family: 'Yu Gothic'; font-size: 16px; }")
            elif sender == self.checkbox2:
                pixmap = QPixmap('code/image/model2.png')
                self.text_label_tab1.setText("animagine-xl-3.1\n　animagine-xl-3.1はLinaqruf氏が発表したイラストモデルです。絵柄が変えやすく画風LoRAへの対応力が優れています。") 
            elif sender == self.checkbox3:
                pixmap = QPixmap('code/image/model3.png')
                self.text_label_tab1.setText("fuduki_mix_v2.0\n　fuduki_mixはこたじろう氏が作成したアジア系の顔立ちの女性の出力に特化したモデルです。比較的簡単に美麗な女性の写真風画像を生成できます。") 
            elif sender == self.checkbox4:
                pixmap = QPixmap('code/image/model4.png')
                self.text_label_tab1.setText("Juggernaut-XL_v9\n　Juggernaut-XL_v9は世界中で多くダウンロードされていて更新が頻繁に行われている写真系のモデルです。リアルなポートレートや背景が得意です。") 
            elif sender == self.checkbox_canny:
                pixmap = QPixmap('code/image/canny.png')
                self.text_label_tab1.setText("canny\n　コントロールネットcannyはエッジ検出を利用して画像の輪郭線を抽出して生成に利用します。元画像の再現度が高めです") 
            elif sender == self.checkbox_depth:
                pixmap = QPixmap('code/image/depth.png')
                self.text_label_tab1.setText("depth\n　コントロールネットdepthは物体までの距離を検出して生成に利用します。人物のみの検出に長けています。") 
            elif sender == self.checkbox_openpose:
                pixmap = QPixmap('code/image/openpose.png')
                self.text_label_tab1.setText("openpose\n　コントロールネットopenposeはカラフルな棒人間のようなもので人間の骨格を検出し生成に利用します。輪郭線や距離を抽出しないため人物のみの容姿や服装を変えることができ自由度が高いです。") 
            elif sender == self.checkbox_softedge:
                pixmap = QPixmap('code/image/softedge.png')
                self.text_label_tab1.setText("softedge\n　コントロールネットsoftedgeは輪郭線を抽出しますがCannyより大まかに取得します。") 
            else:
                pixmap = QPixmap()  # デフォルトの空の画像を設定
                self.text_label.setText("")  # テキストをクリア
            self.image_label_tab1.setPixmap(pixmap)
            self.image_label_tab1.resize(pixmap.size())  # QLabelのサイズを画像のサイズに合わせる

        else:
            # すべてのチェックボックスがオフの場合、画像とテキストをクリア
            self.image_label_tab1.setPixmap(QPixmap())  # チェックがない時は画像をクリア
            self.image_label_tab1.adjustSize()  # QLabelのサイズを内容に合わせて調整
            self.text_label_tab1.setText("")  # テキストをクリア

    # 最後にアクティブだったチェックボックスに基づいて画像を更新
    def on_checkbox_toggled_tab2(self, sender):
        if sender.isChecked():
            if sender == self.checkbox_localization:
                pixmap = QPixmap('code/image/localization.png')
                self.text_label_tab2.setText("localization-JP\n　WebUIの表示を日本語化します。大半の項目は日本語化されますが未対応のものもあります。適用には「settings」→「Apply settings」→「ReloadUI」を押していったんWebUIを閉じます。もう一度ここからインストールを実行すると設定が変更され日本語化されます。")  # テキストの設定
            elif sender == self.checkbox_tagcomplete:
                pixmap = QPixmap('code/image/tagcomplete.png')
                self.text_label_tab2.setText("TagComplete\n　入力するプロンプトの予測変換を表示します。多くのモデルはdanbooruタグという特殊な形式で学習されているため自然な文章では適切ではない可能性があります。英語のスペルを正確に覚えていなくても最初の数文字を入れるだけで目的のプロンプトを入力できます。")  # テキストの設定
            elif sender == self.checkbox_history:
                pixmap = QPixmap('code/image/history.png')
                self.text_label_tab2.setText("history-slider\n　プロンプトを一文字ずつ保存し巻き戻せるようにできます。プロンプトを書いたり消したりしていると特定のところまで巻き戻したいと思うことがあるのでそのような時に便利です。")
            elif sender == self.checkbox_ar:
                pixmap = QPixmap('code/image/ar.png')
                self.text_label_tab2.setText("ar-plus\n　生成する画像のサイズをボタンで変えられるようにします。よく使う画像の縦横比を登録しておけばスライダーを動かさずに設定できます。")
            elif sender == self.checkbox_Presets:
                pixmap = QPixmap('code/image/Presets.png')
                self.text_label_tab2.setText("Config-Presets\n　WebUIを起動する度に設定を初期値から変更するのは面倒です。よく使う設定を登録しておくことで次回起動時にすぐ呼び出すことができます。")  
            elif sender == self.checkbox_adetailer:
                pixmap = QPixmap('code/image/ADetailer.png')
                self.text_label_tab2.setText("ADetailer\n　生成した画像の顔の部分などを自動で検出しよりきれいにします。また、画像を生成してから表情を変えたり眼鏡をかけさせるなど表情差分を作ることもできます")  
            elif sender == self.checkbox_lama:
                pixmap = QPixmap('code/image/lama.png')
                self.text_label_tab2.setText("lama\n　生成した画像から不要なものを消すのに使います。不必要な小物やロゴマーク、テキスト等を消去できます。") 
            elif sender == self.checkbox_pose:
                pixmap = QPixmap('code/image/openpose_editor.png')
                self.text_label_tab2.setText("openpose-editor\n　コントロールネットのopenposeで使えるカラフルな棒人間を編集できます。コントロールネットの本体でも編集はできますが、一から手軽にポーズ指定ができます。") 
            elif sender == self.checkbox_dynamic:
                pixmap = QPixmap('code/image/dynamic.png')
                self.text_label_tab2.setText("dynamic-prompts\n　プロンプトに{ short hair | long hair }と記述すると1/2の確率で長い髪か短い髪が選ばれます。ランダムにプロンプトを選び、変化を持たせたいときに使用します。") 
            elif sender == self.checkbox_weight:
                pixmap = QPixmap('code/image/lora-block-weight.png')
                self.text_label_tab2.setText("lora-block-weight\n　LoRAを階層と呼ばれるブロックから適用量を指定して使用する拡張機能です。プリセットで使用します。") 
            elif sender == self.checkbox_supermerger:
                pixmap = QPixmap('code/image/supermerger.png')
                self.text_label_tab2.setText("supermerger\n　モデルを合成する機能の拡張版です。") 
            else:
                pixmap = QPixmap()  # デフォルトの空の画像を設定
                self.text_label_tab2.setText("")  # テキストをクリア
            self.image_label_tab2.setPixmap(pixmap)
            self.image_label_tab2.resize(pixmap.size())  # QLabelのサイズを画像のサイズに合わせる
        else:
            # すべてのチェックボックスがオフの場合、画像とテキストをクリア
            self.image_label_tab2.setPixmap(QPixmap())  # チェックがない時は画像をクリア
            self.image_label_tab2.adjustSize()  # QLabelのサイズを内容に合わせて調整
            self.text_label_tab2.setText("")  # テキストをクリア

# WebUI(1111版)の拡張機能の画像表示
    # 最後にアクティブだったチェックボックスに基づいて画像を更新
    def on_checkbox_toggled_tab3(self, sender):
        if sender.isChecked():
            if sender == self.checkbox_controlnet1111:
                pixmap = QPixmap('code/image/controlnet.png')
                self.text_label_tab3.setText("controlnet\n　輪郭線や棒人間などの素体を用いて生成画像を制御する手法の総称をコントロールネットといいます。forge版では同梱されていますが、1111版では個別にダウンロードする必要があります。コントロールネットのモデルはforge版と共有できますが適用には「settings」→「Apply settings」→「ReloadUI」を押していったんWebUIを再起動する必要があります。")  # テキストの設定
            elif sender == self.checkbox_localization1111:
                pixmap = QPixmap('code/image/localization.png')
                self.text_label_tab3.setText("localization-JP\n　WebUIの表示を日本語化します。大半の項目は日本語化されますが未対応のものもあります。適用には「settings」→「Apply settings」→「ReloadUI」を押していったんWebUIを閉じます。もう一度ここからインストールを実行すると設定が変更され日本語化されます。")  # テキストの設定
            elif sender == self.checkbox_tagcomplete1111:
                pixmap = QPixmap('code/image/tagcomplete.png')
                self.text_label_tab3.setText("TagComplete\n　入力するプロンプトの予測変換を表示します。多くのモデルはdanbooruタグという特殊な形式で学習されているため自然な文章では適切ではない可能性があります。英語のスペルを正確に覚えていなくても最初の数文字を入れるだけで目的のプロンプトを入力できます。")  # テキストの設定
            elif sender == self.checkbox_history1111:
                pixmap = QPixmap('code/image/history.png')
                self.text_label_tab3.setText("history-slider\n　プロンプトを一文字ずつ保存し巻き戻せるようにできます。プロンプトを書いたり消したりしていると特定のところまで巻き戻したいと思うことがあるのでそのような時に便利です。")
            elif sender == self.checkbox_ar1111:
                pixmap = QPixmap('code/image/ar.png')
                self.text_label_tab3.setText("ar-plus\n　生成する画像のサイズをボタンで変えられるようにします。よく使う画像の縦横比を登録しておけばスライダーを動かさずに設定できます。")
            elif sender == self.checkbox_Presets1111:
                pixmap = QPixmap('code/image/Presets.png')
                self.text_label_tab3.setText("Config-Presets\n　WebUIを起動する度に設定を初期値から変更するのは面倒です。よく使う設定を登録しておくことで次回起動時にすぐ呼び出すことができます。")  
            elif sender == self.checkbox_adetailer1111:
                pixmap = QPixmap('code/image/ADetailer.png')
                self.text_label_tab3.setText("ADetailer\n　生成した画像の顔の部分などを自動で検出しよりきれいにします。また、画像を生成してから表情を変えたり眼鏡をかけさせるなど表情差分を作ることもできます")  
            elif sender == self.checkbox_lama1111:
                pixmap = QPixmap('code/image/lama.png')
                self.text_label_tab3.setText("lama\n　生成した画像から不要なものを消すのに使います。不必要な小物やロゴマーク、テキスト等を消去できます。") 
            elif sender == self.checkbox_pose1111:
                pixmap = QPixmap('code/image/openpose_editor.png')
                self.text_label_tab3.setText("openpose-editor\n　コントロールネットのopenposeで使えるカラフルな棒人間を編集できます。コントロールネットの本体でも編集はできますが、一から手軽にポーズ指定ができます。") 
            elif sender == self.checkbox_dynamic1111:
                pixmap = QPixmap('code/image/dynamic.png')
                self.text_label_tab3.setText("dynamic-prompts\n　プロンプトに{ short hair | long hair }と記述すると1/2の確率で長い髪か短い髪が選ばれます。ランダムにプロンプトを選び、変化を持たせたいときに使用します。") 
            elif sender == self.checkbox_weight1111:
                pixmap = QPixmap('code/image/lora-block-weight.png')
                self.text_label_tab3.setText("lora-block-weight\n　LoRAを階層と呼ばれるブロックから適用量を指定して使用する拡張機能です。プリセットで使用します。") 
            elif sender == self.checkbox_supermerger1111:
                pixmap = QPixmap('code/image/supermerger.png')
                self.text_label_tab3.setText("supermerger\n　モデルを合成する機能の拡張版です。") 
            else:
                pixmap = QPixmap()  # デフォルトの空の画像を設定
                self.text_label_tab3.setText("")  # テキストをクリア
            self.image_label_tab3.setPixmap(pixmap)
            self.image_label_tab3.resize(pixmap.size())  # QLabelのサイズを画像のサイズに合わせる
        else:
            # すべてのチェックボックスがオフの場合、画像とテキストをクリア
            self.image_label_tab3.setPixmap(QPixmap())  # チェックがない時は画像をクリア
            self.image_label_tab3.adjustSize()  # QLabelのサイズを内容に合わせて調整
            self.text_label_tab3.setText("")  # テキストをクリア

# ダウンロードを実行する
    def start_download(self):
        forge_repo = "https://github.com/lllyasviel/stable-diffusion-webui-forge.git"
        repo_dir = "stable-diffusion-webui-forge"
        # レポジトリのディレクトリが既に存在するか確認
        if not os.path.exists(repo_dir):
            print("Stable Diffusion WebUI Forgeをダウンロードします...")
            subprocess.run(["git", "clone", forge_repo], check=True)
        else:
            print(f"{repo_dir} は既に存在します。次のステップに進みます。")

        # 「stable-diffusion-webui-forge」にディレクトリを移動
        os.chdir("stable-diffusion-webui-forge")
        # styles.csvファイルのパスを構築
        styles_path = "styles.csv"
        # styles.csvファイルが存在するかチェック
        if not os.path.exists(styles_path):
            try:
                # styles.csvファイルを新規作成し、ヘッダーと空白行を追加
                with open(styles_path, "w", encoding="utf-8") as file:
                    file.write("name,prompt,negative_prompt\n")
                    file.write("\n")
                print("新しいstyles.csvファイルが作成されました。")
            except Exception as e:
                print("styles.csvファイルの作成中にエラーが発生しました:")
                print(str(e))
        else:
            print("styles.csvファイルが既に存在するため、処理をスキップします。")
        os.chdir("models\Stable-diffusion")

        if self.checkbox0.isChecked():
            if not os.path.exists("hanamomopony_v14.safetensors"):
                print("hanamomopony_v14をダウンロードします")
                subprocess.run(["curl", "-L", "https://huggingface.co/kataragi/AIGen/resolve/main/XLmodel/hanamomopony_v14.safetensors", "-o", "hanamomopony_v14.safetensors", "--progress-bar"], check=True)
            # 二階層上のディレクトリを取得
            current_dir = os.getcwd()
            parent_dir = os.path.dirname(current_dir)
            grandparent_dir = os.path.dirname(parent_dir)
            # styles.csvファイルのパスを構築
            styles_path = os.path.join(grandparent_dir, "styles.csv")
            # 所定のテキスト
            text_to_append = "hanamomopony_v14,\"score_9, score_8_up, score_7_up, source_anime, \",\"deformed anatomy, deformed fingers, realistic, source_furry, censored, @_@, heart-shaped pupils, abs, \""
            try:
                # styles.csvファイルを読み込む
                with open(styles_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                # 所定のテキストを末尾に挿入
                lines.append(text_to_append + "\n")
                # styles.csvファイルを更新
                with open(styles_path, "w", encoding="utf-8") as file:
                    file.writelines(lines)
                print("styles.csvファイルが更新されました。")
            except FileNotFoundError:
                print("styles.csvファイルが見つかりませんでした。")
            except Exception as e:
                print("エラーが発生しました:")
                print(str(e))
        else:
            print("momoiropony_v14は既にダウンロードされています")

        if self.checkbox1.isChecked():
            if not os.path.exists("momoiropony_v14.safetensors"):
                print("momoiropony_v14をダウンロードします")
                subprocess.run(["curl", "-L", "https://huggingface.co/kataragi/AIGen/resolve/main/XLmodel/momoiropony_v14.safetensors", "-o", "momoiropony_v14.safetensors", "--progress-bar"], check=True)
            # 二階層上のディレクトリを取得
            current_dir = os.getcwd()
            parent_dir = os.path.dirname(current_dir)
            grandparent_dir = os.path.dirname(parent_dir)
            # styles.csvファイルのパスを構築
            styles_path = os.path.join(grandparent_dir, "styles.csv")
            # 所定のテキスト
            text_to_append = "momoiropony_v14,\"score_9, score_8_up, score_7_up, source_anime, \",\"deformed anatomy, deformed fingers, realistic, source_furry, censored, @_@, heart-shaped pupils, abs, \""
            try:
                # styles.csvファイルを読み込む
                with open(styles_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                # 所定のテキストを末尾に挿入
                lines.append(text_to_append + "\n")
                # styles.csvファイルを更新
                with open(styles_path, "w", encoding="utf-8") as file:
                    file.writelines(lines)
                print("styles.csvファイルが更新されました。")
            except FileNotFoundError:
                print("styles.csvファイルが見つかりませんでした。")
            except Exception as e:
                print("エラーが発生しました:")
                print(str(e))
        else:
            print("momoiropony_v14は既にダウンロードされています")

        if self.checkbox2.isChecked():
            if not os.path.exists("animagine-xl-3.1.safetensors"):
                print("animagine-xl-3.1.safetensorsをダウンロードします")
                subprocess.run(["curl", "-L", "https://huggingface.co/kataragi/AIGen/resolve/main/XLmodel/animagine-xl-3.1.safetensors", "-o", "animagine-xl-3.1.safetensors", "--progress-bar"], check=True)
            # 二階層上のディレクトリを取得
            current_dir = os.getcwd()
            parent_dir = os.path.dirname(current_dir)
            grandparent_dir = os.path.dirname(parent_dir)
            # styles.csvファイルのパスを構築
            styles_path = os.path.join(grandparent_dir, "styles.csv")
            # 所定のテキスト
            text_to_append = "animagine-xl-3.1,\"masterpiece, best quality, very aesthetic, absurdres, \",\"lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]\""
            try:
                # styles.csvファイルを読み込む
                with open(styles_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                # 所定のテキストを末尾に挿入
                lines.append(text_to_append + "\n")
                # styles.csvファイルを更新
                with open(styles_path, "w", encoding="utf-8") as file:
                    file.writelines(lines)
                print("styles.csvファイルが更新されました。")
            except FileNotFoundError:
                print("styles.csvファイルが見つかりませんでした。")
            except Exception as e:
                print("エラーが発生しました:")
                print(str(e))
        else:
            print("animagine-xl-3.1は既にダウンロードされています")

        if self.checkbox3.isChecked():
            if not os.path.exists("fuduki_mix_v20.safetensors"):
                print("fuduki_mix_v2をダウンロードします")
                subprocess.run(["curl", "-L", "https://huggingface.co/kataragi/AIGen/resolve/main/XLmodel/fuduki_mix_v20.safetensors", "-o", "fuduki_mix_v20.safetensors", "--progress-bar"], check=True)
            # 二階層上のディレクトリを取得
            current_dir = os.getcwd()
            parent_dir = os.path.dirname(current_dir)
            grandparent_dir = os.path.dirname(parent_dir)
            # styles.csvファイルのパスを構築
            styles_path = os.path.join(grandparent_dir, "styles.csv")
            # 所定のテキスト
            text_to_append = "fuduki_mix_v20,\"japanese woman, (natural lighting), \",\"(cleavage:2), (illustration), 3d, 2d, painting, cartoons, sketch, watercolor, monotone,(kimono), (crossed eyes), (strabismus)\""
            try:
                # styles.csvファイルを読み込む
                with open(styles_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                # 所定のテキストを末尾に挿入
                lines.append(text_to_append + "\n")
                # styles.csvファイルを更新
                with open(styles_path, "w", encoding="utf-8") as file:
                    file.writelines(lines)
                print("styles.csvファイルが更新されました。")
            except FileNotFoundError:
                print("styles.csvファイルが見つかりませんでした。")
            except Exception as e:
                print("エラーが発生しました:")
                print(str(e))
        else:
            print("fuduki_mix_v2は既にダウンロードされています")

        if self.checkbox4.isChecked():
            if not os.path.exists("Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors"):
                print("Juggernaut-XL_v9をダウンロードします")
                subprocess.run(["curl", "-L", "https://huggingface.co/kataragi/AIGen/resolve/main/XLmodel/Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors", "-o", "Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors", "--progress-bar"], check=True)
            # 二階層上のディレクトリを取得
            current_dir = os.getcwd()
            parent_dir = os.path.dirname(current_dir)
            grandparent_dir = os.path.dirname(parent_dir)
            # styles.csvファイルのパスを構築
            styles_path = os.path.join(grandparent_dir, "styles.csv")
            # 所定のテキスト
            text_to_append = "Juggernaut-XL_v9,\", \",\"CGI, Unreal, Airbrushed, Digital\""
            try:
                # styles.csvファイルを読み込む
                with open(styles_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                # 所定のテキストを末尾に挿入
                lines.append(text_to_append + "\n")
                # styles.csvファイルを更新
                with open(styles_path, "w", encoding="utf-8") as file:
                    file.writelines(lines)
                print("styles.csvファイルが更新されました。")
            except FileNotFoundError:
                print("styles.csvファイルが見つかりませんでした。")
            except Exception as e:
                print("エラーが発生しました:")
                print(str(e))
        else:
            print("Juggernaut-XL_v9は既にダウンロードされています")

        # 現在のディレクトリから一階層上に移動
        os.chdir("..")
        # 「ControlNet」フォルダーを作成
        if not os.path.exists("ControlNet"):
                os.mkdir("ControlNet")
        else:
            print("ControlNetフォルダーは既に存在します。")
        # 「ControlNet」ディレクトリに移動
        os.chdir("ControlNet")

        def download_file(url, destination):
            response = requests.get(url, stream=True)
            response.raise_for_status()
            # 不成功なステータスコードを返したHTTPリクエストの場合、HTTPErrorを発生させます
            with open(destination, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

        if self.checkbox_canny.isChecked():
            destination = "controlnet_xl_canny.safetensors" # 保存先のファイル名
            if not os.path.exists(destination):
                print("cannyをダウンロードします")
                file_url = "https://huggingface.co/kataragi/AIGen/resolve/main/XLControlnet/diffusers_xl_canny_full.safetensors"
                download_file(file_url, destination) # ファイルをダウンロードするために関数を呼び出します
                print(f"{destination}にファイルをダウンロードしました。")
            else:
                print("cannyは既にダウンロードされています")

        if self.checkbox_depth.isChecked():
            destination = "controlnet_xl_depth.safetensors" # 保存先のファイル名
            if not os.path.exists(destination):
                print("depthをダウンロードします")
                file_url = "https://huggingface.co/kataragi/AIGen/resolve/main/XLControlnet/diffusers_xl_depth_full.safetensors"
                download_file(file_url, destination) # ファイルをダウンロードするために関数を呼び出します
                print(f"{destination}にファイルをダウンロードしました。")
            else:
                print("depthは既にダウンロードされています")

        if self.checkbox_openpose.isChecked():
            destination = "controlnet_xl_openpose.safetensors" # 保存先のファイル名
            if not os.path.exists(destination):
                print("openposeをダウンロードします")
                file_url = "https://huggingface.co/kataragi/AIGen/resolve/main/XLControlnet/thibaud_xl_openpose.safetensors"
                download_file(file_url, destination) # ファイルをダウンロードするために関数を呼び出します
                print(f"{destination}にファイルをダウンロードしました。")
            else:
                print("openposeは既にダウンロードされています")

        if self.checkbox_softedge.isChecked():
            destination = "controlnet_xl_softedge.safetensors" # 保存先のファイル名
            if not os.path.exists(destination):
                print("softedgeをダウンロードします")
                file_url = "https://huggingface.co/kataragi/AIGen/resolve/main/XLControlnet/sargezt_xl_softedge.safetensors"
                download_file(file_url, destination) # ファイルをダウンロードするために関数を呼び出します
                print(f"{destination}にファイルをダウンロードしました。")
            else:
                print("softedgeは既にダウンロードされています")

        # 現在のディレクトリから二階層上に移動
        os.chdir(os.path.join("..", ".."))
        # 「extensions」フォルダーに移動
        os.chdir("extensions")
        tabs_repo = "https://github.com/Haoming02/sd-webui-tabs-extension.git"
        civitai_repo = "https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper.git"


        localization_repo = "https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP.git"
        tagcomplete_repo = "https://github.com/DominikDoom/a1111-sd-webui-tagcomplete.git"
        history_slider_repo = "https://github.com/LucasMali/sd-history-slider.git"
        ar_plus_repo = "https://github.com/LEv145/--sd-webui-ar-plus.git"
        dialogue_repo = "https://github.com/w-e-w/sdwebui-close-confirmation-dialogue.git"
        Presets_repo = "https://github.com/Zyin055/Config-Presets.git"
        adetailer_repo = "https://github.com/Bing-su/adetailer.git"
        lama_repo = "https://github.com/aka7774/sd_lama_cleaner.git"
        pose_repo = "https://github.com/fkunn1326/openpose-editor.git"
        dynamic_repo = "https://github.com/adieyal/sd-dynamic-prompts.git"

        weigh_repo = "https://github.com/hako-mikan/sd-webui-lora-block-weight.git"
        supermerger = "https://github.com/hako-mikan/sd-webui-supermerger.git"

        # リポジトリをダウンロード
        print("タブまとめ機能ダウンロードしています...")
        if subprocess.call(["git", "clone", tabs_repo]) != 0:
            print("タブまとめ機能は既にダウンロードされています。")

        print("Civitaiヘルパーをダウンロードしています...")
        if subprocess.call(["git", "clone", civitai_repo]) != 0:
            print("Civitaiヘルパーは既にダウンロードされています。")

        print("confirmation-dialogueをダウンロードしています...")
        if subprocess.call(["git", "clone", Presets_repo]) != 0:
            print("confirmation-dialogueは既にダウンロードされています。")

        if self.checkbox_localization.isChecked():
            print("日本語化をダウンロードしています...")
            if subprocess.call(["git", "clone", localization_repo]) != 0:
                print("日本語化は既にダウンロードされています。")
                # 現在のディレクトリを取得
                current_directory = os.getcwd()
                print(current_directory)
                try:
                    # 一階層上のディレクトリのパスを取得
                    parent_dir = os.path.dirname(os.getcwd())
                    config_path = os.path.join(parent_dir, "config.json")
                    # 合成された「config.json」のあるディレクトリを取得
                    config_dir = os.path.dirname(config_path)
                    # 合成された「config.json」のあるディレクトリを表示
                    print("「config.json」のあるディレクトリ:", config_dir)
                    # config.jsonファイルが存在するかチェック
                    if not os.path.exists(config_path):
                        print("config.jsonファイルが見つかりませんでした。")
                        return
                    # config.jsonファイルを読み込む
                    with open(config_path, "r", encoding="utf-8") as file:
                        config_data = json.load(file)
                    # "localization"の値を"ja_JP"に変更
                    config_data["localization"] = "ja_JP"
                    # config.jsonファイルを更新
                    with open(config_path, "w", encoding="utf-8") as file:
                        json.dump(config_data, file, indent=4)
                    print("config.jsonファイルの更新が完了しました。")
                except Exception as e:
                    print("エラーが発生しました:")
                    print(str(e))

        if self.checkbox_tagcomplete.isChecked():
            print("tagcompleteをダウンロードしています...")
            if subprocess.call(["git", "clone", tagcomplete_repo]) != 0:
                print("tagcompleteは既にダウンロードされています。")

        if self.checkbox_history.isChecked():
            print("history-sliderをダウンロードしています...")
            if subprocess.call(["git", "clone", history_slider_repo]) != 0:
                print("history-sliderは既にダウンロードされています。")

        if self.checkbox_ar.isChecked():
            print("ar-plusをダウンロードしています...")
            if subprocess.call(["git", "clone", ar_plus_repo]) == 0:
                print("ar-plusのダウンロードに成功しました。")
                # 二階層上の「code」フォルダーに移動
                if os.path.exists("../../code/resolutions.txt"):
                    shutil.copy("../../code/resolutions.txt", "--sd-webui-ar-plus")
                    print("resolutions.txtのコピーが完了しました。")
                else:
                    print("resolutions.txtが見つかりませんでした。")
                # 「aspect_ratios.txt」をコピー
                if os.path.exists("../../code/aspect_ratios.txt"):
                    shutil.copy("../../code/aspect_ratios.txt", "--sd-webui-ar-plus")
                    print("aspect_ratios.txtのコピーが完了しました。")
                else:
                    print("aspect_ratios.txtが見つかりませんでした。")
            else:
                print("ar-plusは既にダウンロードされています。")

        if self.checkbox_Presets.isChecked():
            print("Config-Presetsをダウンロードしています...")
            if subprocess.call(["git", "clone", Presets_repo]) != 0:
                print("Config-Presetsは既にダウンロードされています。")
                # 「config-txt2img.json」のコピー処理
                if os.path.exists("../../code/config-txt2img.json"):
                    shutil.copy("../../code/config-txt2img.json", "Config-Presets")
                    print("config-txt2img.jsonのコピーが完了しました。")

        if self.checkbox_adetailer.isChecked():
            print("adetailerをダウンロードしています...")
            if subprocess.call(["git", "clone", adetailer_repo]) != 0:
                print("adetailerは既にダウンロードされています。")

        if self.checkbox_lama.isChecked():
            print("lama_cleanerをダウンロードしています...")
            if subprocess.call(["git", "clone", lama_repo]) != 0:
                print("lama_cleanerは既にダウンロードされています。")

        if self.checkbox_pose.isChecked():
            print("openpose-editorをダウンロードしています...")
            if subprocess.call(["git", "clone", pose_repo]) != 0:
                print("openpose-editorは既にダウンロードされています。")

        if self.checkbox_dynamic.isChecked():
            print("dynamic-promptsをダウンロードしています...")
            if subprocess.call(["git", "clone", dynamic_repo]) != 0:
                print("dynamic-promptsは既にダウンロードされています。")

        if self.checkbox_weight.isChecked():
            print("lora-block-weighをダウンロードしています...")
            if subprocess.call(["git", "clone", weigh_repo]) != 0:
                print("lora-block-weighは既にダウンロードされています。")

        if self.checkbox_supermerger.isChecked():
            print("supermergerをダウンロードしています...")
            if subprocess.call(["git", "clone", supermerger_repo]) != 0:
                print("supermergerは既にダウンロードされています。")

        # 現在のディレクトリから２階層上に移動
        os.chdir(os.path.join("..",".."))
        # 現在のディレクトリを取得
        current_directory = os.getcwd()
        print(current_directory)
        # 新しいコマンドコンソールを開き、webui.batを非同期に実行
        # subprocess.Popen(["start", "cmd", "/c", "webui.bat"], shell=True)
        QMessageBox.information(self, "ダウンロード完了", "ファイルのダウンロードが完了しました。")

# stable-diffusion-webui(forge版)を更新する
    def git_pull_forge(self):
        # 現在のディレクトリを取得
        current_directory = os.getcwd()
        print(current_directory)
        repo_path = "stable-diffusion-webui-forge"
        # リポジトリのディレクトリに移動
        os.chdir(repo_path)
        # git pull コマンドを実行
        try:
            result = subprocess.run(["git", "pull"], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("更新が正常に完了しました。")
            os.chdir(os.path.join(".."))
            return result.stdout, result.stderr
        except subprocess.CalledProcessError as e:
            print("更新でエラーが発生しました。")
            os.chdir(os.path.join(".."))
            return e.stdout, e.stderr
        # 現在のディレクトリを取得
        current_directory = os.getcwd()
        print(current_directory)

# stable-diffusion-webui(forge版)を起動する
    def launch_webui(self):
        # 現在のディレクトリを取得
        current_directory = os.getcwd()
        print(current_directory)
        # webui-user.batを非同期に実行
        subprocess.Popen(["start", "cmd", "/c", "webui-user.bat"], cwd="stable-diffusion-webui-forge", shell=True)

# current_directory = os.getcwd() # 現在のディレクトリを取得
# print(current_directory)

# stable-diffusion-webui(1111版)を起動する
    def launch_webui1111(self):
        bat_file_path = "stable-diffusion-webui\\webui-user.bat"
        new_line = "set COMMANDLINE_ARGS="
        if self.radio_button1.isChecked(): # Forge版とモデルを共有する場合の処理
            current_directory = os.getcwd() # 現在のディレクトリを取得
            print(current_directory)
            # radio_button1が選択されている場合、特定のコマンドライン引数を追加
            new_line += "--xformers --ckpt-dir \"../stable-diffusion-webui-forge/models/Stable-diffusion\" --lora-dir \"../stable-diffusion-webui-forge/models/Lora\" --embeddings-dir \"../stable-diffusion-webui-forge/embeddings\""
            
            print("Forge版とモデルを共有するコマンドライン引数に更新されました")
        else:
            print("1111版のモデルを使用するコマンドライン引数に更新されました")
        # radio_button2が選択されている場合、一つの引数のみを追加
            new_line += "--xformers"
        # 元の .bat ファイルの内容を読み込む
        with open(bat_file_path, "r") as file:
            lines = file.readlines()
        # COMMANDLINE_ARGSを含む行を置き換える
        with open(bat_file_path, "w") as file:
            for line in lines:
                if line.startswith("set COMMANDLINE_ARGS="):
                    file.write(new_line + "\n")
                else:
                    file.write(line)

        def update_config_file(config_path, new_path):
            # Configファイルが存在するかチェック
            config_path = "stable-diffusion-webui/config.json"
            if not os.path.exists(config_path):
                print("Configファイルが存在しないため、更新をスキップします。")
                return
            # ファイルの内容を読み込む
            with open(config_path, "r") as file:
                lines = file.readlines()
            # 目的の行が見つかったかどうかを追跡するためのフラグ
            found = False
            # 特定の行を更新
            with open(config_path, "w") as file:
                for line in lines:
                    if '"control_net_models_path":' in line:
                        # 行を修正
                        line = f'    "control_net_models_path": "{new_path}",\n'
                        found = True
                    file.write(line)
            if found:
                print("Configファイルが更新されました。")
            else:
                print("Configファイル内に目的の行が見つからなかったため、変更はありません。")

        # Configファイルへのパス
        config_file_path = "path/to/stable-diffusion-webui/config.json"
        # 設定する新しいパス
        new_models_path = "../stable-diffusion-webui-forge/models/ControlNet"
        # Configファイルを更新する関数を呼び出す
        update_config_file(config_file_path, new_models_path)

        # webui-user.batを非同期に実行
        subprocess.Popen(["start", "cmd", "/c", "webui-user.bat"], cwd="stable-diffusion-webui", shell=True)

# stable-diffusion-webui(1111版)を更新する
    def git_pull_webui1111(self):
        # 現在のディレクトリを取得
        current_directory = os.getcwd()
        print(current_directory)
        repo_path = "stable-diffusion-webui"
        # リポジトリのディレクトリに移動
        os.chdir(repo_path)
        # git pull コマンドを実行
        try:
            result = subprocess.run(["git", "pull"], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("更新が正常に完了しました。")
            os.chdir(os.path.join(".."))
            return result.stdout, result.stderr
        except subprocess.CalledProcessError as e:
            print("更新でエラーが発生しました。")
            os.chdir(os.path.join(".."))
            return e.stdout, e.stderr
        # 現在のディレクトリを取得
        current_directory = os.getcwd()
        print(current_directory)

# stable-diffusion-webui(1111版)をダウンロードする
    def start_download1111(self):
        webui_repo = "https://github.com/AUTOMATIC1111/stable-diffusion-webui.git"
        repo_dir = "stable-diffusion-webui"
        # レポジトリのディレクトリが既に存在するか確認
        if not os.path.exists(repo_dir):
            print("Stable Diffusion WebUI(1111版)をダウンロードします...")
            subprocess.run(["git", "clone", webui_repo], check=True)
        else:
            print(f"{repo_dir} は既に存在します。次のステップに進みます。")

        # 「stable-diffusion-webui」にディレクトリを移動
        os.chdir("stable-diffusion-webui")
        # styles.csvファイルのパスを構築
        styles_path = "styles.csv"
        # styles.csvファイルが存在するかチェック
        if not os.path.exists(styles_path):
            try:
                # styles.csvファイルを新規作成し、ヘッダーと空白行を追加
                with open(styles_path, "w", encoding="utf-8") as file:
                    file.write("name,prompt,negative_prompt\n")
                    file.write("\n")
                print("新しいstyles.csvファイルが作成されました。")
            except Exception as e:
                print("styles.csvファイルの作成中にエラーが発生しました:")
                print(str(e))
        else:
            print("styles.csvファイルが既に存在するため、処理をスキップします。")

        os.chdir("models\Stable-diffusion")
        folder_path = os.getcwd()
        specific_string0 = 'hanamomopony_v14'
        specific_string1 = 'momoiropony'
        specific_string2 = 'animagine-xl-3.1'
        specific_string3 = 'fuduki_mix'
        specific_string4 = 'Juggernaut-XL'
        # フォルダが存在し、かつディレクトリであることを確認
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            # フォルダ内のファイル名を取得
            files = os.listdir(folder_path)
            # 各ファイルについて特定の文字列が含まれているか確認し、ラベルを更新
            file_contains_string = any(specific_string0 in file for file in files)
            # 所定のテキスト
            text_to_append = "hanamomopony_v14,\"score_9, score_8_up, score_7_up, source_anime, \",\"deformed anatomy, deformed fingers, realistic, source_furry, censored, @_@, heart-shaped pupils, abs, \""
            try:
                # styles.csvファイルを読み込む
                with open(styles_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                # 所定のテキストを末尾に挿入
                lines.append(text_to_append + "\n")
                # styles.csvファイルを更新
                with open(styles_path, "w", encoding="utf-8") as file:
                    file.writelines(lines)
                print("styles.csvファイルが更新されました。")
            except FileNotFoundError:
                print("styles.csvファイルが見つかりませんでした。")
            except Exception as e:
                print("エラーが発生しました:")
                print(str(e))
            file_contains_string = any(specific_string1 in file for file in files)
            # 所定のテキスト
            text_to_append = "momoiropony_v14,\"score_9, score_8_up, score_7_up, source_anime, \",\"deformed anatomy, deformed fingers, realistic, source_furry, censored, @_@, heart-shaped pupils, abs, \""
            try:
                # styles.csvファイルを読み込む
                with open(styles_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                # 所定のテキストを末尾に挿入
                lines.append(text_to_append + "\n")
                # styles.csvファイルを更新
                with open(styles_path, "w", encoding="utf-8") as file:
                    file.writelines(lines)
                print("styles.csvファイルが更新されました。")
            except FileNotFoundError:
                print("styles.csvファイルが見つかりませんでした。")
            except Exception as e:
                print("エラーが発生しました:")
                print(str(e))
            file_contains_string = any(specific_string2 in file for file in files)
            # 所定のテキスト
            text_to_append = "animagine-xl-3.1,\"masterpiece, best quality, very aesthetic, absurdres, \",\"lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]\""
            try:
                # styles.csvファイルを読み込む
                with open(styles_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                # 所定のテキストを末尾に挿入
                lines.append(text_to_append + "\n")
                # styles.csvファイルを更新
                with open(styles_path, "w", encoding="utf-8") as file:
                    file.writelines(lines)
                print("styles.csvファイルが更新されました。")
            except FileNotFoundError:
                print("styles.csvファイルが見つかりませんでした。")
            except Exception as e:
                print("エラーが発生しました:")
                print(str(e))
            file_contains_string = any(specific_string3 in file for file in files)
            # 所定のテキスト
            text_to_append = "fuduki_mix_v20,\"japanese woman, (natural lighting), \",\"(cleavage:2), (illustration), 3d, 2d, painting, cartoons, sketch, watercolor, monotone,(kimono), (crossed eyes), (strabismus)\""
            try:
                # styles.csvファイルを読み込む
                with open(styles_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                # 所定のテキストを末尾に挿入
                lines.append(text_to_append + "\n")
                # styles.csvファイルを更新
                with open(styles_path, "w", encoding="utf-8") as file:
                    file.writelines(lines)
                print("styles.csvファイルが更新されました。")
            except FileNotFoundError:
                print("styles.csvファイルが見つかりませんでした。")
            except Exception as e:
                print("エラーが発生しました:")
                print(str(e))
            file_contains_string = any(specific_string4 in file for file in files)
            # 所定のテキスト
            text_to_append = "Juggernaut-XL_v9,\", \",\"CGI, Unreal, Airbrushed, Digital\""
            try:
                # styles.csvファイルを読み込む
                with open(styles_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                # 所定のテキストを末尾に挿入
                lines.append(text_to_append + "\n")
                # styles.csvファイルを更新
                with open(styles_path, "w", encoding="utf-8") as file:
                    file.writelines(lines)
                print("styles.csvファイルが更新されました。")
            except FileNotFoundError:
                print("styles.csvファイルが見つかりませんでした。")
            except Exception as e:
                print("エラーが発生しました:")
                print(str(e))

        # 現在のディレクトリから二階層上に移動
        os.chdir(os.path.join("..", ".."))
        os.chdir("extensions") # 「extensions」フォルダーに移動
        tabs_repo = "https://github.com/Haoming02/sd-webui-tabs-extension.git"
        civitai_repo = "https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper.git"
        controlnet_repo = "https://github.com/lllyasviel/ControlNet.git"
        localization_repo = "https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP.git"
        tagcomplete_repo = "https://github.com/DominikDoom/a1111-sd-webui-tagcomplete.git"
        history_slider_repo = "https://github.com/LucasMali/sd-history-slider.git"
        ar_plus_repo = "https://github.com/LEv145/--sd-webui-ar-plus.git"
        dialogue_repo = "https://github.com/w-e-w/sdwebui-close-confirmation-dialogue.git"
        Presets_repo = "https://github.com/Zyin055/Config-Presets.git"
        adetailer_repo = "https://github.com/Bing-su/adetailer.git"
        lama_repo = "https://github.com/aka7774/sd_lama_cleaner.git"
        pose_repo = "https://github.com/fkunn1326/openpose-editor.git"
        dynamic_repo = "https://github.com/adieyal/sd-dynamic-prompts.git"
        
        weigh_repo = "https://github.com/hako-mikan/sd-webui-lora-block-weight.git"
        supermerger = "https://github.com/hako-mikan/sd-webui-supermerger.git"

        # リポジトリをダウンロード
        print("タブまとめ機能ダウンロードしています...")
        if subprocess.call(["git", "clone", tabs_repo]) != 0:
            print("タブまとめ機能は既にダウンロードされています。")

        print("Civitaiヘルパーをダウンロードしています...")
        if subprocess.call(["git", "clone", civitai_repo]) != 0:
            print("Civitaiヘルパーは既にダウンロードされています。")

        print("confirmation-dialogueをダウンロードしています...")
        if subprocess.call(["git", "clone", Presets_repo]) != 0:
            print("confirmation-dialogueは既にダウンロードされています。")

        if self.checkbox_controlnet1111.isChecked():
            print("controlnetをダウンロードしています...")
            if subprocess.call(["git", "clone", controlnet_repo]) != 0:
                print("controlnetは既にダウンロードされています。")

        if self.checkbox_localization1111.isChecked():
            print("日本語化をダウンロードしています...")
            if subprocess.call(["git", "clone", localization_repo]) != 0:
                print("日本語化は既にダウンロードされています。")
                # 現在のディレクトリを取得
                current_directory = os.getcwd()
                print(current_directory)
                try:
                    # 一階層上のディレクトリのパスを取得
                    parent_dir = os.path.dirname(os.getcwd())
                    config_path = os.path.join(parent_dir, "config.json")
                    # 合成された「config.json」のあるディレクトリを取得
                    config_dir = os.path.dirname(config_path)
                    # 合成された「config.json」のあるディレクトリを表示
                    print("「config.json」のあるディレクトリ:", config_dir)
                    # config.jsonファイルが存在するかチェック
                    if not os.path.exists(config_path):
                        print("config.jsonファイルが見つかりませんでした。")
                        return
                    # config.jsonファイルを読み込む
                    with open(config_path, "r", encoding="utf-8") as file:
                        config_data = json.load(file)
                    # "localization"の値を"ja_JP"に変更
                    config_data["localization"] = "ja_JP"
                    # config.jsonファイルを更新
                    with open(config_path, "w", encoding="utf-8") as file:
                        json.dump(config_data, file, indent=4)
                    print("config.jsonファイルの更新が完了しました。")
                except Exception as e:
                    print("エラーが発生しました:")
                    print(str(e))

        if self.checkbox_tagcomplete1111.isChecked():
            print("tagcompleteをダウンロードしています...")
            if subprocess.call(["git", "clone", tagcomplete_repo]) != 0:
                print("tagcompleteは既にダウンロードされています。")

        if self.checkbox_history1111.isChecked():
            print("history-sliderをダウンロードしています...")
            if subprocess.call(["git", "clone", history_slider_repo]) != 0:
                print("history-sliderは既にダウンロードされています。")

        if self.checkbox_ar1111.isChecked():
            print("ar-plusをダウンロードしています...")
            if subprocess.call(["git", "clone", ar_plus_repo]) == 0:
                print("ar-plusのダウンロードに成功しました。")
                # 二階層上の「code」フォルダーに移動
                if os.path.exists("../../code/resolutions.txt"):
                    shutil.copy("../../code/resolutions.txt", "--sd-webui-ar-plus")
                    print("resolutions.txtのコピーが完了しました。")
                else:
                    print("resolutions.txtが見つかりませんでした。")
                # 「aspect_ratios.txt」をコピー
                if os.path.exists("../../code/aspect_ratios.txt"):
                    shutil.copy("../../code/aspect_ratios.txt", "--sd-webui-ar-plus")
                    print("aspect_ratios.txtのコピーが完了しました。")
                else:
                    print("aspect_ratios.txtが見つかりませんでした。")
            else:
                print("ar-plusは既にダウンロードされています。")

        if self.checkbox_Presets1111.isChecked():
            print("Config-Presetsをダウンロードしています...")
            if subprocess.call(["git", "clone", Presets_repo]) != 0:
                print("Config-Presetsは既にダウンロードされています。")
                # 「config-txt2img.json」のコピー処理
                if os.path.exists("../../code/config-txt2img.json"):
                    shutil.copy("../../code/config-txt2img.json", "Config-Presets")
                    print("resolutions.txtのコピーが完了しました。")

        if self.checkbox_adetailer1111.isChecked():
            print("adetailerをダウンロードしています...")
            if subprocess.call(["git", "clone", adetailer_repo]) != 0:
                print("adetailerは既にダウンロードされています。")

        if self.checkbox_lama1111.isChecked():
            print("lama_cleanerをダウンロードしています...")
            if subprocess.call(["git", "clone", lama_repo]) != 0:
                print("lama_cleanerは既にダウンロードされています。")

        if self.checkbox_pose1111.isChecked():
            print("openpose-editorをダウンロードしています...")
            if subprocess.call(["git", "clone", pose_repo]) != 0:
                print("openpose-editorは既にダウンロードされています。")

        if self.checkbox_dynamic1111.isChecked():
            print("dynamic-promptsをダウンロードしています...")
            if subprocess.call(["git", "clone", dynamic_repo]) != 0:
                print("dynamic-promptsは既にダウンロードされています。")

        if self.checkbox_weight1111.isChecked():
            print("lora-block-weighをダウンロードしています...")
            if subprocess.call(["git", "clone", weigh_repo]) != 0:
                print("lora-block-weighは既にダウンロードされています。")

        if self.checkbox_supermerger1111.isChecked():
            print("supermergerをダウンロードしています...")
            if subprocess.call(["git", "clone", supermerger_repo]) != 0:
                print("supermergerは既にダウンロードされています。")

        # ディレクトリをもとの場所に戻す
        os.chdir(os.path.join("..", ".."))
        # 現在のディレクトリを取得
        current_directory = os.getcwd()
        print(current_directory)
        # 新しいコマンドコンソールを開き、webui.batを非同期に実行
        # subprocess.Popen(["start", "cmd", "/c", "webui.bat"], shell=True)
        QMessageBox.information(self, "ダウンロード完了", "ファイルのダウンロードが完了しました。")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())