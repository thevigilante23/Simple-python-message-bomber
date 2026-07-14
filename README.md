# Message Automation CLI

A lightweight Python command-line tool built with **PyAutoGUI** for learning desktop automation. It allows users to automate keyboard input with configurable messages, repetition counts, and delays.

> ⚠️ **Disclaimer**
>
> This project was created for **educational purposes** to learn Python, command-line interfaces, and desktop automation. Use it responsibly and **only on applications or systems where you have permission to automate input**. The author is not responsible for misuse of this software.

---

## Features

* ⌨️ Automated keyboard input with PyAutoGUI
* 🔁 Configurable repetition count
* ⏱️ Adjustable delay between messages
* 📊 Progress indicator
* 🛑 Safe interruption using `Ctrl + C`

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Install the required dependency:

```bash
pip install pyautogui
```

---

## Usage

Basic usage:

```bash
python bomb.py -i "Hello World" -n 10
```

Specify a delay:

```bash
python bomb.py -i "Hello World" -n 20 -d 1
```

### Arguments

| Argument        | Description                                        |
| --------------- | -------------------------------------------------- |
| `-i`, `--msg`   | Message to send                                    |
| `-n`, `--no`    | Number of repetitions                              |
| `-d`, `--delay` | Delay between repetitions (default: `0.5` seconds) |

---

## Example

```bash
python bomb.py -i "Hello" -n 5 -d 0.5
```

---

## Technologies Used

* Python 3
* PyAutoGUI
* argparse

---


---

## License

This project is released for educational purposes. Please use it responsibly and respect the rules of any platform or application where you automate input.
