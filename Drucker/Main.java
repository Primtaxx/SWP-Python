public class Main {
    public static void main(String[] args) {
        // Initialisiere Drucker
        Drucker swDrucker = new SWDrucker();
        Drucker colorDrucker = new ColorDrucker();

        // Initialisiere Proxy
        DruckerProxy druckerProxy = new DruckerProxy(swDrucker);

        // SW-Druck
        druckerProxy.drucken("Dokument 1");

        // Wechsle zu Farbdrucker
        druckerProxy.switchTo(colorDrucker);

        // Farbdruck
        druckerProxy.drucken("Dokument 2");

        // Wechsle zu SW-Drucker
        druckerProxy.switchTo(swDrucker);

        // SW-Druck
        druckerProxy.drucken("Dokument 3");
    }
}
