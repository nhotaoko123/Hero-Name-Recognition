# League of Legends: Wild Rift - Hero Recognition in Highlight Moments

## Introduction

League of Legends: Wild Rift (also known as Wild Rift) is a multiplayer online battle arena (MOBA) game developed by Riot Games. In this project, we focus on developing a highlight moment detection system specifically tailored for Wild Rift. This system is designed to recognize and identify heroes appearing on the message bar during intense battles, which is crucial for understanding key moments in the game.

## Objective

The main objective of this project is to create a reliable and accurate system that can:
- Detect highlight moments during gameplay.
- Recognize the specific hero mentioned in the message bar when a battle occurs.
- Enhance the analysis of game footage by automatically identifying critical moments and the heroes involved.

## Features

- Hero Detection: Automatically detects and identifies heroes based on the text displayed in the message bar during battles.
- Highlight Moment Analysis: Pinpoints crucial moments in the game, aiding in better game analysis and content creation.
- Scalability: Designed to be scalable and adaptable for different versions of Wild Rift as the game evolves.

## For example:


| Image              | Hero name                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| ![image](https://github.com/user-attachments/assets/fbfb3d0f-077e-4ac6-ba3a-d87a56bedc1e) | Ahri  |
| ![image](https://github.com/user-attachments/assets/1009e2b8-50d5-47ab-9c5a-fa3723169e62) | Ashe  |


    • hero_names.txt: All hero names of Wild Rift.
    • test_images/: image for testing.
    • test.txt: groundtruth of each image in test_iamges/ folder. Each record in this file has the format: <input_filename> <hero_name>.
