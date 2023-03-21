{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOwgLfwJ92rfDJJcO2OXIMo",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/TUTUTU0817/streamlit-scrapper-Query/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 375
        },
        "id": "PDSaw8wpOitu",
        "outputId": "9a27ca36-9132-4a12-de46-f4069b7d2be7"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-b72eccf9b215>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;31m# read data, 讀取資料\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "\n",
        "# read data, 讀取資料\n",
        "\n",
        "df=pd.read_csv(\"TWSE_TW-1.csv\")\n",
        "df.fillna('', inplace=True)\n",
        "\n",
        "# set up Streamlit app, 建立應用程式\n",
        "st.title(\"TWSE Stock Search, 台灣股票代號查詢\")\n",
        "\n",
        "# add search box and dropdown, 增加搜尋選擇欄位\n",
        "search_term = st.text_input(\"Enter search term, 輸入查詢資料:\")\n",
        "search_by = st.selectbox(\"Search by column:\", options=['Symbol 公司代碼', 'Name 公司名稱'])\n",
        "\n",
        "# search for matching rows, 搜尋並列印結果\n",
        "if search_term:\n",
        "    if search_by == 'Symbol 公司代碼':\n",
        "        result = df[df['Symbol'].str.contains(search_term)]\n",
        "    elif search_by == 'Name 公司名稱':\n",
        "        result = df[df['Name'].str.contains(search_term)]\n",
        "    else:\n",
        "        result = pd.DataFrame()\n",
        "    st.write('Search ',search_term,' by ', search_by )   \n",
        "    st.write(result)\n",
        "    "
      ]
    }
  ]
}