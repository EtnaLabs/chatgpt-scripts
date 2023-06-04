# ChatGPT Tips and Tricks

Welcome 👋!

This repo is a collection of tips, tricks, scripts, and tools that we use at EtnaLabs to optimize the development flow
with ChatGPT.

Whether you're new to ChatGPT or a seasoned pro-user, this repository aims to provide valuable resources to enhance your
experience.

## Makefile Commands
Copy the Makefile into your directory and use the following commands.

### gpt-update-filepaths
This command updates Python and NodeJS files in your project `.py|.js|.ts|.tsx`, 
adding at the top a comment that indicate the filepath. This is very helpful for your copy/paste in ChatGPT. Run it with the following make command:
```bash
make gpt-update-filepath
```
🐦 https://twitter.com/feulf/status/1664360181168328707

### gpt-context
This command provide ChatGPT with the context of your NodeJS and Python projects. It provides information
about the project tree and the packages, which you can copy to the clipboard and use in your ChatGPT conversations.  Run it with the following make command:
  ```bash
  make gpt-context
  ```
🐦 https://twitter.com/feulf/status/1661472705802297344


Feel free to modify the Makefile and add more commands to suit your specific needs.

We hope these scripts and tools help you optimize your development flow with ChatGPT. Contributions and feedback are
welcome!

## License

This repository is licensed under the MIT License. See the LICENSE file for more information.

If you have any questions or need further assistance, please don't hesitate to reach out. Enjoy coding with ChatGPT 🤖🦾🚀!!