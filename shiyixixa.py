{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/babbi1/bd/blob/master/shiyixixa.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "id": "8VKwQiV9iY0f",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 179
        },
        "outputId": "a71d2c2f-3897-44f5-e321-46c9c3b55858"
      },
      "cell_type": "code",
      "source": [
        "def bmr():\n",
        "    print('您好，我可以帮您计算基础代谢率；')\n",
        "    a=input('需要计算请输入\"bmr\",如退出请输入\"q\"：')\n",
        "\n",
        "    while a=='bmr' or a=='BMR':\n",
        "        print(\"请输入以下信息，空格分割\")\n",
        "        str=input(\"性别 体重(kg） 身高（cm） 年龄：\")\n",
        "        strlist=str.split(\" \")\n",
        "        print(strlist)\n",
        "        print('您是{}性,今年{}岁，重{}kg,身高{}cm对吗？'.format(strlist[0],strlist[-1],strlist[1],strlist[2]))\n",
        "        xb = strlist[0]\n",
        "        nl = float(strlist[-1])\n",
        "        tz = float(strlist[1])\n",
        "        sg = float(strlist[-1])\n",
        "        if xb=='男':\n",
        "            bmrna = (13.7 * tz) + (5.0 * sg) - ( 6.8 * nl)+66\n",
        "            print('您的基础代谢率为：',bmrna)\n",
        "        elif xb == '女':\n",
        "            bmrnv = (9.6 * tz) + (1.0 * sg) - (4.7 * nl)+655\n",
        "            print('您的基础代谢率为：',bmrnv)\n",
        "        a=input('需要计算请输入\"bmr\",如退出请输入\"q\"：')\n",
        "\n",
        "    else:\n",
        "        input(\"退出请按回车\")\n",
        "\n",
        "bmr()"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "您好，我可以帮您计算基础代谢率；\n",
            "需要计算请输入\"bmr\",如退出请输入\"q\"：bmr\n",
            "请输入以下信息，空格分割\n",
            "性别 体重(kg） 身高（cm） 年龄：男 50 176 24\n",
            "['男', '50', '176', '24']\n",
            "您是男性,今年24岁，重50kg,身高176cm对吗？\n",
            "您的基础代谢率为： 707.8\n",
            "需要计算请输入\"bmr\",如退出请输入\"q\"：环境\n",
            "退出请按回车\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}