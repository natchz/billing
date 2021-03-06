package xades4j.production;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileOutputStream;

import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.junit.Test;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import static xades4j.production.VerifyXadesProc.VerifyXadesProcess;
import xades4j.properties.DataObjectDesc;

import xades4j.utils.DOMHelper;

import xades4j.providers.KeyingDataProvider;
import xades4j.providers.impl.FileSystemKeyStoreKeyingDataProvider;
import xades4j.providers.impl.FirstCertificateSelector;
import xades4j.providers.impl.DirectPasswordProvider;
import xades4j.providers.SignaturePolicyInfoProvider;

import xades4j.properties.IdentifierType;
import xades4j.properties.ObjectIdentifier;
import xades4j.properties.SignaturePolicyBase;
import xades4j.properties.SignaturePolicyIdentifierProperty;
import xades4j.properties.SignerRoleProperty;
import xades4j.properties.SigningTimeProperty;
import xades4j.providers.SignaturePropertiesCollector;
import xades4j.providers.SignaturePropertiesProvider;
import xades4j.verification.VerifierTestBase;
import xades4j.verification.XadesVerifierImplTest;
import xades4j.utils.SignatureServicesTestBase;
import static xades4j.utils.SignatureServicesTestBase.toPlatformSpecificFilePath;


public class main {
    private static final String FOLDER = "C:/Users/german/PycharmProjects/billing/java_xades";
    private static final String CERT = "certs.p12";
    private static final String PASS = "Opsol123";

    private static final String DOCUMENT = "C:/Users/german/PycharmProjects/billing/inv.xml";

    public static void main(String[] args) throws Exception {
        System.setProperty("org.apache.xml.security.ignoreLineBreaks", "true");

        System.out.println("    ====> Firmando XML");
        signEpes();
    }

private static void signEpes() throws Exception {
    Document doc = null;

    DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
    dbf.setNamespaceAware(true);
    DocumentBuilder db = dbf.newDocumentBuilder();
    doc = db.parse(new File(DOCUMENT));

    Element elem = doc.getDocumentElement();
    DOMHelper.useIdAsXmlId(elem);

    KeyingDataProvider kdp = new FileSystemKeyStoreKeyingDataProvider( "pkcs12",
                        CERT_FOLDER + CERT,
                        new FirstCertificateSelector(),
                        new DirectPasswordProvider(PASS),
                        new DirectPasswordProvider(PASS),
                        true);

    // politica
    SignaturePolicyInfoProvider policyInfoProvider = new SignaturePolicyInfoProvider() {
        @Override
        public SignaturePolicyBase getSignaturePolicy() {
            try {
                return new SignaturePolicyIdentifierProperty(
                        new ObjectIdentifier("http://www.facturae.es/politica_de_firma_formato_facturae/politica_de_firma_formato_facturae_v3_1.pdf",
                                             IdentifierType.URI,
                                             "Política de firma para facturas electrónicas de la República de Colombia"),
                        new ByteArrayInputStream(Files.readAllBytes(Paths.get(POLICY)))
                );
            } catch (IOException ex) {
                Logger.getLogger(FirmaFec.class.getName()).log(Level.SEVERE, null, ex);
            }
            return null;
        }
    };

    // Role
    SignerEPES signer = (SignerEPES) new XadesEpesSigningProfile(kdp, policyInfoProvider)
               .withSignaturePropertiesProvider(new SignaturePropertiesProvider() {
                   @Override
                   public void provideProperties(SignaturePropertiesCollector arg0) {
                       SigningTimeProperty sigTime = new SigningTimeProperty();
                       arg0.setSignerRole(new SignerRoleProperty().withClaimedRole("supplier"));
                       arg0.setSigningTime(sigTime );
                   }
               })
          .newSigner();

   new Enveloped(signer).sign(elem);
   TransformerFactory tFactory = TransformerFactory.newInstance();
   Transformer transformer = tFactory.newTransformer();
   DOMSource source = new DOMSource(doc);
   StreamResult result = new StreamResult(new File(SIGNED));

   transformer.transform (source, result);
}

    protected static void outputDocument(Document doc, String fileName) throws Exception
    {
        TransformerFactory tf = TransformerFactory.newInstance();
        File outDir = ensureOutputDir();
        FileOutputStream out = new FileOutputStream(new File(outDir, fileName));
        tf.newTransformer().transform(
                new DOMSource(doc),
                new StreamResult(out));
        out.close();
    }

    private static File ensureOutputDir()
    {
        File dir = new File(toPlatformSpecificFilePath(FOLDER));
        dir.mkdir();
        return dir;
    }

}