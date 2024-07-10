#import BlynkLibESP32 as BlynkLib   # for ESP32
import BlynkLib as BlynkLib


BLYNK_AUTH="ntDBx7-dkNt7gT3A6nTx4xoKBhwEw71F"
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH, insecure=True)

# start Blynk (this call should never return)
blynk.run()
