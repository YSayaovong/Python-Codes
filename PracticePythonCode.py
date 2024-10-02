{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "f7c0d886"
   },
   "source": [
    "# Activity: Practice writing Python code"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "0c066c48"
   },
   "source": [
    "## Introduction\n",
    "\n",
    "Python is a programming language that helps in automating instructions to the computer in a variety of contexts, including security contexts. Writing code in Python is a valuable skill that helps security analysts thrive in their technical work.\n",
    "\n",
    "In this lab, you'll practice writing your first Python code while learning about a notebook environment. The hands-on practice you engage in throughout the labs will help you apply Python coding skills to your work as a security analyst. You'll benefit the most from the labs if you make sure to not only write in the cells that you're prompted to fill in, but also analyze all the cells thoroughly."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "c5e84779"
   },
   "source": [
    "<details><summary><h2>Tips for completing this lab</h2></summary>\n",
    "\n",
    "As you navigate this lab, keep the following tips in mind:\n",
    "\n",
    "- `### YOUR CODE HERE ###` indicates where you should write code. Be sure to replace this with your own code before running the code cell.\n",
    "- Feel free to open the hints for additional guidance as you work on each task.\n",
    "- To enter your answer to a question, double-click the markdown cell to edit. Be sure to replace the \"[Double-click to enter your responses here.]\" with your own answer.\n",
    "- You can save your work manually by clicking File and then Save in the menu bar at the top of the notebook.\n",
    "- You can download your work locally by clicking File and then Download and then specifying your preferred file format in the menu bar at the top of the notebook.\n",
    "</details>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "cf55e108"
   },
   "source": [
    "## Scenario\n",
    "\n",
    "As a security analyst, you'll often use notebook environments and notebooks to write and run code. This lab will help you get familiar with working in a notebook environment, writing code comments in Python, and displaying strings with the print() function.\n",
    "\n",
    "In this lab, you'll complete a series of tasks that involve observing and running some pre-written cells of text and code, as well as filling in cells with your own text, Python code, and code comments."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "dddf9066"
   },
   "source": [
    "## Task 1\n",
    "\n",
    "The lab environment you're working in is a notebook-based coding environment. Notebooks, such as this one, consist of two types of cells: (1) text cells, also known as markdown cells, and (2) code cells.\n",
    "\n",
    "Markdown cells allow you to write plain text and format it in the markdown language. Markdown language is used for formatting plain text in text editors and code editors. For example, you can use markdown to make headers, bold or italicize words, format text as code, add hyperlinks, and more.\n",
    "\n",
    "For this task, write something into the following markdown cell. Be sure to replace the \"[Double-click to edit this markdown cell and write something here.]\" with your own text. When you have finished editing, press the Shift and Enter keys (or on some keyboards, the Shift and Return keys) to display your text."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I have replaced the placeholder text with my own. This notebook is helping me understand how to work with markdown cells and Python code cells in a notebook environment."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "87404578"
   },
   "source": [
    "<details>\n",
    "  <summary><h4><strong>Hint 1</strong></h4></summary>\n",
    "\n",
    "Double-click the markdown cell and replace the placeholder statement with your own. You can write any statement of your choice.\n",
    "\n",
    "</details>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "64d3dfd5"
   },
   "source": [
    "## Task 2\n",
    "In Python notebooks, code cells allow you to write code comments and code in Python.\n",
    "\n",
    "To run a code cell, first place your cursor on the cell. Then, you can either click on the play icon, or press the Shift and Enter keys (or on some keyboards, the Shift and Return keys).\n",
    "\n",
    "For this task, run the following code cell as is and observe the output."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "04268ef8"
   },
   "outputs": [],
   "source": [
    "# This cell displays \"Hello world!\"\n",
    "print(\"Hello world!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "87404578"
   },
   "source": [
    "<details>\n",
    "  <summary><h4><strong>Hint 1</strong></h4></summary>\n",
    "\n",
    "Once you click on the code cell, you can run the code by either clicking on the triangular play icon, or press the Shift and Enter keys (or on some keyboards, the Shift and Return keys).\n",
    "\n",
    "</details>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### **Question 1**\n",
    "**What do you observe about the output after you ran the code cell?**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The output is the text \"Hello world!\" printed on the screen. The code successfully executed the print() function, displaying the string provided within the parentheses."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5cb83fb8"
   },
   "source": [
    "## Task 3\n",
    "\n",
    "Writing code comments is a way to document the intention behind code. It's a standard that analysts commonly use in their workflow. Writing comments that accompany code allows you to keep track of the technical decisions you've made in your project. This makes it easier for you and your team to read and revisit your code in order to understand what it does and why you took certain approaches.\n",
    "\n",
    "For this task, run the following code cell as is and observe the output."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "e837a2e5"
   },
   "outputs": [],
   "source": [
    "# In Python, comments do not get displayed\n",
    "# This code cell contains only comments"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "a0990885"
   },
   "source": [
    "<details>\n",
    "    <summary><h4><strong>Hint 1</strong></h4></summary>\n",
    "\n",
    "Once you click on the code cell, you can run the code by either clicking on the triangular play icon, or press the Shift and Enter keys (or on some keyboards, the Shift and Return keys).\n",
    "\n",
    "</details>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "94d7173f"
   },
   "source": [
    "#### **Question 2**\n",
    "**What do you observe about the output after you ran the cell above?**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "35cebec3"
   },
   "source": [
    "There is no output displayed because the cell only contains comments. Python ignores comments during execution, so nothing is shown when the cell is run."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5dc33cf4"
   },
   "source": [
    "## Task 4\n",
    "\n",
    "To type in a code cell, first click into the cell. Then you can write comments and code inside the cell.\n",
    "\n",
    "For this task, add a comment at the beginning of the following code cell, describing what the code is doing. Write the comment to say `# This cell displays \"I am using Python.\"`. Be sure to replace the `# YOUR COMMENT HERE` with your own comment before running the following cell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "fdd233bd"
   },
   "outputs": [],
   "source": [
    "# This cell displays \"I am using Python.\"\n",
    "print(\"I am using Python.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "a0990885"
   },
   "source": [
    "<details>\n",
    "    <summary><h4><strong>Hint 1</strong></h4></summary>\n",
    "\n",
    "Once you click into the code cell, replace the placeholder comment with your comment. Recall that comments in Python start with the hash symbol (`#`).\n",
    "\n",
    "</details>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ffe34587"
   },
   "source": [
    "#### **Question 3**\n",
    "**What do you observe about the output after you ran the cell above?**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "8f2a5fa7"
   },
   "source": [
    "The output is the text \"I am using Python.\" printed on the screen. The comment I added was not displayed, but the print() function executed correctly."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "406daa6d"
   },
   "source": [
    "## Task 5\n",
    "In Python, `print()` helps you to display information to the screen.\n",
    "\n",
    "For this task, use `print()` to display the message `\"I am a security analyst.\"` by placing that message within the parentheses. Be sure to replace the `### YOUR CODE HERE ###` with your own code before running the following code cell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "id": "edcd0fe6"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I am a security analyst.\n"
     ]
    }
   ],
   "source": [
    "print(\"I am a security analyst.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "26dfef63"
   },
   "source": [
    "<details>\n",
    "    <summary><h4><strong>Hint 1</strong></h4></summary>\n",
    "\n",
    "\n",
    "Once you click into the code cell, replace the `### YOUR CODE HERE ###` with `\"I am a security analyst.\"`.\n",
    "\n",
    "</details>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "bf8d3259"
   },
   "source": [
    "#### **Question 4**\n",
    "**What do you observe about the output after you ran the cell above?**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "b5ee2b89"
   },
   "source": [
    "The output is the text \"I am a security analyst.\" printed on the screen, as expected. The print() function successfully displayed the string provided."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "8f119729"
   },
   "source": [
    "## Task 6\n",
    "For this task, write a `print()` statement to display the string `\"Python is useful for security!\"` Be sure to replace the `### YOUR CODE HERE ###` with your own code before running the following code cell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "fe43a1fc"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python is useful for security!\n"
     ]
    }
   ],
   "source": [
    "print(\"Python is useful for security!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5a669a55"
   },
   "source": [
    "<details>\n",
    "    <summary><h4><strong>Hint 1</strong></h4></summary>\n",
    "\n",
    "Click into the code cell and use `print()` to display the message.\n",
    "\n",
    "</details>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "b43c14e3"
   },
   "source": [
    "<details>\n",
    "    <summary><h4><strong>Hint 2</strong></h4></summary>\n",
    "\n",
    "Place the message inside the parentheses of `print()`.\n",
    "\n",
    "</details>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "bf8d3259"
   },
   "source": [
    "#### **Question 5**\n",
    "**What do you observe about the output after you ran the cell above?**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "b5ee2b89"
   },
   "source": [
    "The output is the text \"Python is useful for security!\" printed on the screen. The print() function worked as intended, displaying the string."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "563f6d9c"
   },
   "source": [
    "## Task 7\n",
    "For your final task, you'll combine all the `print()` statements you've encountered and written in this lab up to this point, into one code cell.\n",
    "\n",
    "Complete the following code with the remaining messages. Be sure to replace each `### YOUR CODE HERE ###` with your own code before running the following cell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "ddd374cf"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world!\n",
      "I am using Python.\n",
      "I am a security analyst.\n",
      "Python is useful for security!\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello world!\")\n",
    "print(\"I am using Python.\")\n",
    "print(\"I am a security analyst.\")\n",
    "print(\"Python is useful for security!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "f131bcb9"
   },
   "source": [
    "<details>\n",
    "    <summary><h4><strong>Hint 1</strong></h4></summary>\n",
    "\n",
    "First click into the code cell.\n",
    "\n",
    "For the third `print()` statement, place the string `\"I am a security analyst.\"` inside the parantheses of `print()`.\n",
    "\n",
    "For the fourth `print()` statement, place the string `\"Python is useful for security!\"` inside the parantheses of `print()`.\n",
    "\n",
    "</details>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "bf8d3259"
   },
   "source": [
    "#### **Question 6**\n",
    "**What do you observe about the output after you ran the cell above?**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "dcbb0f5f"
   },
   "source": [
    "The output consists of all the strings from the previous print statements, each printed on a new line:\n",
    "\"Hello world!\"\n",
    "\"I am using Python.\"\n",
    "\"I am a security analyst.\"\n",
    "\"Python is useful for security!\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "d47250b6"
   },
   "source": [
    "## Conclusion\n",
    "**What are your key takeaways from this lab?**\n",
    "\n",
    "The lab provided a clear introduction to working in a notebook environment, using markdown for text formatting, and writing basic Python code. It emphasized the importance of comments for code documentation and demonstrated how the print() function is used to display output."
   ]
  }
 ],
 "metadata": {
  "colab": {
   "provenance": [
    {
     "file_id": "1KtE2DAbz5pj_IP34uE9K5nils1RUHVKg",
     "timestamp": 1667953394971
    }
   ]
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}