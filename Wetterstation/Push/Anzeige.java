package Wetterstation.Push;

public class Anzeige implements Observer {
    private float temperature;
    private float humidity;

    @Override
    public void update(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        display();
    }

    public void display() {
        System.out.println("Temperatur: " + temperature + " °C, Luftfeuchtigkeit: " + humidity + " %");
    }
}