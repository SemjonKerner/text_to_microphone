# text_to_microphone

This repository contains a proof of concept that allows text-to-speech(TTS) conversion with an absolute minimum interface.
This enables participation in video conferences / tele conferences without having or using a microphone.

The Interface consists of only an text entry field and nothing more. Writing text is as easy as it gets.
Sending Text to a TTS server is done with **Tab**, **Return** or **Keypad-Return**.

There is also a simple LIFO history that can be manouvered with **Up** and **Down** Arrowkeys. **Escape** will allways bring you back to the empty text entry field.

This said, expect bugs.

However you still have to do routing on your on (using setup.sh to create virtual sinks and pavucontrol to route these).
To setup the routing follow this guide: https://endless.ersoft.org/pulseaudio-loopback/
