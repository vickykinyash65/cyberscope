# CyberScope

## Overview

CyberScope is a Python-based tool designed to encrypt data transmissions on Windows systems to ensure secure and private communication. It utilizes symmetric encryption to safeguard messages sent over a network, making it ideal for enhancing security in your applications.

## Features

- **Encryption**: Encrypts data using the Fernet symmetric encryption mechanism from the `cryptography` library.
- **Decryption**: Decrypts received data to retrieve the original message.
- **Networking**: Sends and receives encrypted messages over a network using Python's `socket` library.

## Requirements

- Python 3.6 or higher
- `cryptography` library (install with `pip install cryptography`)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/cyberscope.git
   cd cyberscope
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

   (Note: You need to create a `requirements.txt` file with the line `cryptography` in it if you haven't already.)

## Usage

### Start the Server

Run the following command to start the server and listen for incoming encrypted messages:

```bash
python cyberscope.py
```

Edit the code to specify the host and port in the `start_server` method.

### Send a Message

To send an encrypted message, modify the `send_message` method parameters and execute:

```bash
python cyberscope.py
```

## Security Considerations

- Ensure the key used for encryption is kept secret and secure.
- This program is designed for educational purposes; always assess the security for real-world applications.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any feature additions or bug fixes.