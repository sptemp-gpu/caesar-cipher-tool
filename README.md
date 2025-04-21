# Caesar Cipher Tool

A tool for encrypting and decrypting text using various encryption methods like Caesar Cipher, Vigenère Cipher, and AES. This tool also supports batch file processing, cloud storage integration (future), and more.

![GitHub](https://img.shields.io/github/license/sptemp/caesar-cipher-tool)
![Version](https://img.shields.io/github/v/release/sptemp/caesar-cipher-tool)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
 
## Features

- Encrypt and decrypt text using Caesar Cipher, Vigenère Cipher, and AES.
- Load and save files for batch processing.
- Real-time feedback and help options for new users.
- Future cloud storage integration.
- Log actions and errors for tracking.

## Installation

Clone the repo and install dependencies:


- git clone https://github.com/yourusername/caesar-cipher-tool.git
- cd caesar-cipher-tool
- pip install -r requirements.txt


## Usage

### Caesar Cipher
To encrypt text using Caesar Cipher:
1. Enter the text to be encrypted.
2. Specify the shift value (an integer).
3. Click 'Encrypt' to get the encrypted text.

To decrypt, follow the same steps, but use the negative value of the shift.

### Vigenère Cipher
For encrypting text using the Vigenère Cipher:
1. Enter the text to be encrypted.
2. Provide a key (string).
3. Click 'Encrypt' to get the encrypted text.

For decryption, the key is the same, and the tool will reverse the encryption process.

### AES Encryption
For AES encryption:
1. Enter the text you want to encrypt.
2. Provide a password for encryption (this will be the AES key).
3. Click 'Encrypt' to get the encrypted text.

For decryption, the AES password is required to decrypt the text.

### File Operations
- You can load and save encrypted text to/from files.
- Batch processing: You can also load multiple files for encryption/decryption in bulk.

### Real-time Help
The tool also includes a help option that explains how to use the tool for beginners.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for the libraries and resources.
- Inspired by cryptographic algorithms and techniques.

## Future Features

- Cloud storage integration (future).
- Multi-language support (future).
- Real-time collaboration for shared encryption/decryption tasks.
