from playbulbcandle import PlayBulbCandle

# Example addresses, discover yours with `hcitool lescan`
addresses = ['AC:E6:4B:07:EE:6B','AC:E6:4B:08:1C:74', 'AC:E6:4B:07:F0:65']

bulbs = [
	PlayBulbCandle(addresses[0]),
	PlayBulbCandle(addresses[1]),
	PlayBulbCandle(addresses[2])
]

bulbs[0].setColor(0, 255, 0, 0)
bulbs[1].setColor(0, 0, 255, 0)
bulbs[2].setColor(0, 0, 0, 255)

#bulbs[0].setEffect(0, 255, 0, 0, 'candle', 0);
#bulbs[1].setEffect(0, 0, 255, 0, 'candle', 0);
#bulbs[2].setEffect(0, 0, 0, 255, 'candle', 0);

for bulb in bulbs:
	print bulb.getBatteryLevel()
	bulb.off();
