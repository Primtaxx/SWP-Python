public class DruckerProxy implements Drucker {
    private Drucker drucker;

    public DruckerProxy(Drucker drucker) {
        this.drucker = drucker;
    }

    public void switchTo(Drucker drucker) {
        this.drucker = drucker;
    }

    @Override
    public void drucken(String dokument) {
        drucker.drucken(dokument);
    }
}
