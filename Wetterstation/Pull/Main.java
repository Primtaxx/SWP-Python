package Wetterstation.Pull;

public class Main {
    public static void main(String[] args) {
        Wetterstation wetterstation = new Wetterstation();

        Anzeige anzeige1 = new Anzeige(wetterstation);
        Anzeige anzeige2 = new Anzeige(wetterstation);

        wetterstation.setMeasurements(25.5f, 65f);
        wetterstation.setMeasurements(26f, 70f);
    }
}