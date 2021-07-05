{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPQHZbcGYPttxGrm46F8gWu",
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
        "<a href=\"https://colab.research.google.com/github/lester48/Cyber_Security_bootcamp/blob/main/GenerateOfHashStringData.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "L5FzhpzGZ5th",
        "outputId": "a96cccf0-7515-419b-a92d-5a4b40bf5f18",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "import hashlib\n",
        "\n",
        "str = \"hello world\"\n",
        "output =  hashlib.md5(str.encode())\n",
        "print(\"The Desired hash is: \")\n",
        "print(output.hexdigest())"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "The Desired hash is: \n",
            "5eb63bbbe01eeed093cb22bb8f5acdc3\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}