package Wetterstation.Pull;


public class Anzeige implements Observer {
    private float temperature;
    private float humidity;
    private Wetterstation wetterstation;

    public Anzeige(Wetterstation wetterstation) {
        this.wetterstation = wetterstation;
        wetterstation.registerObserver(this);
    }

    @Override
    public void update() {
        this.temperature = wetterstation.getTemperature();
        this.humidity = wetterstation.getHumidity();
        display();
    }

    public void display() {
        System.out.println("Temperatur: " + temperature + " °C, Luftfeuchtigkeit: " + humidity + " %");
    }
}

