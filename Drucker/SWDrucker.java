public class SWDrucker implements Drucker {
    @Override
    public void drucken(String dokument) {
        System.out.println("SW-Druck: " + dokument);
    }
}

