read_sensor : read_sensor.c 
	gcc -o read_sensor -lwiringPi -lwiringPiDev

clean : 
	rm *.o read_sensor
