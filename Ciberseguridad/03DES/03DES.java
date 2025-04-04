import javax.swing.*;
import java.io.*;
import java.security.*;
import javax.crypto.*;
import java.awt.*;
import java.awt.event.*;

public class MainGUI {

    private static SecretKey clave;

    public static void main(String[] args) {
        // Crear la ventana principal
        JFrame frame = new JFrame("Cifrado y Descifrado DES");
        frame.setSize(800, 600);  // Tamaño de la ventana
        frame.setLocationRelativeTo(null); // Centrar la ventana
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Crear un panel para contener los componentes
        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());  // Usar un BorderLayout
        panel.setBackground(new Color(45, 45, 45)); // Fondo oscuro
        frame.add(panel);

        // Título en la parte superior
        JLabel titleLabel = new JLabel("Cifrado y Descifrado con DES", JLabel.CENTER);
        titleLabel.setFont(new Font("Arial", Font.BOLD, 22));
        titleLabel.setForeground(Color.WHITE);
        titleLabel.setBackground(new Color(0, 123, 255)); // Color de fondo azul
        titleLabel.setOpaque(true);
        titleLabel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10)); // Bordes alrededor del título
        panel.add(titleLabel, BorderLayout.NORTH);

        // Crear el panel de controles (botones, campos)
        JPanel controlPanel = new JPanel();
        controlPanel.setLayout(new GridBagLayout());
        controlPanel.setBackground(new Color(60, 60, 60)); // Fondo gris oscuro
        panel.add(controlPanel, BorderLayout.CENTER);

        // Llamar a la función para colocar los componentes
        placeComponents(controlPanel);

        // Hacer visible la ventana
        frame.setVisible(true);
    }

    private static void placeComponents(JPanel panel) {
        // Usamos GridBagConstraints para un control detallado del layout
        GridBagConstraints constraints = new GridBagConstraints();
        constraints.insets = new Insets(10, 10, 10, 10); // Espaciado entre los componentes

        // Etiqueta para la carga del archivo
        JLabel fileLabel = new JLabel("Selecciona un archivo:");
        fileLabel.setFont(new Font("Arial", Font.PLAIN, 14));
        fileLabel.setForeground(Color.WHITE); // Texto blanco
        constraints.gridx = 0;
        constraints.gridy = 0;
        constraints.gridwidth = 1;
        panel.add(fileLabel, constraints);

        // Campo de texto para mostrar la ruta del archivo seleccionado
        JTextField filePathField = new JTextField(30);
        filePathField.setFont(new Font("Arial", Font.PLAIN, 14));
        filePathField.setBackground(new Color(200, 200, 200)); // Fondo claro
        filePathField.setForeground(Color.BLACK); // Texto oscuro
        constraints.gridx = 1;
        constraints.gridy = 0;
        panel.add(filePathField, constraints);

        // Botón para seleccionar el archivo
        JButton selectButton = new JButton("Seleccionar");
        selectButton.setFont(new Font("Arial", Font.PLAIN, 14));
        selectButton.setBackground(new Color(0, 123, 255)); // Color azul
        selectButton.setForeground(Color.WHITE); // Texto blanco
        selectButton.setFocusPainted(false); // Quitar el borde al hacer foco
        constraints.gridx = 2;
        constraints.gridy = 0;
        panel.add(selectButton, constraints);

        // Botón para cifrar
        JButton encryptButton = new JButton("Cifrar");
        encryptButton.setFont(new Font("Arial", Font.PLAIN, 14));
        encryptButton.setBackground(new Color(40, 167, 69)); // Verde
        encryptButton.setForeground(Color.WHITE); // Texto blanco
        encryptButton.setFocusPainted(false); // Quitar el borde al hacer foco
        constraints.gridx = 0;
        constraints.gridy = 1;
        panel.add(encryptButton, constraints);

        // Botón para descifrar
        JButton decryptButton = new JButton("Descifrar");
        decryptButton.setFont(new Font("Arial", Font.PLAIN, 14));
        decryptButton.setBackground(new Color(220, 53, 69)); // Rojo
        decryptButton.setForeground(Color.WHITE); // Texto blanco
        decryptButton.setFocusPainted(false); // Quitar el borde al hacer foco
        constraints.gridx = 1;
        constraints.gridy = 1;
        panel.add(decryptButton, constraints);

        // Área de texto para mostrar el resultado del cifrado/descifrado
        JTextArea resultArea = new JTextArea(12, 50);  // Aumentar el tamaño de la área de texto
        resultArea.setFont(new Font("Arial", Font.PLAIN, 14));
        resultArea.setEditable(false);  // No editable
        resultArea.setBackground(new Color(230, 230, 230)); // Fondo claro para el área de texto
        resultArea.setForeground(Color.BLACK); // Texto oscuro
        JScrollPane scrollPane = new JScrollPane(resultArea);
        constraints.gridx = 0;
        constraints.gridy = 2;
        constraints.gridwidth = 3;  // Ocupa las tres columnas
        constraints.fill = GridBagConstraints.HORIZONTAL;  // Rellenar toda la línea
        panel.add(scrollPane, constraints);

        // Acción para seleccionar el archivo
        selectButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser fileChooser = new JFileChooser();
                fileChooser.setDialogTitle("Selecciona un archivo de texto");
                fileChooser.setFileFilter(new javax.swing.filechooser.FileNameExtensionFilter("Archivos de texto", "txt"));
                int result = fileChooser.showOpenDialog(null);
                if (result == JFileChooser.APPROVE_OPTION) {
                    File selectedFile = fileChooser.getSelectedFile();
                    filePathField.setText(selectedFile.getAbsolutePath());
                }
            }
        });

        // Acción para cifrar el archivo
        encryptButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String filePath = filePathField.getText();
                File archivoEntrada = new File(filePath);

                if (!archivoEntrada.exists()) {
                    resultArea.setText("El archivo no existe.");
                    return;
                }

                try {
                    // Generar las claves DES
                    KeyGenerator generadorDES = KeyGenerator.getInstance("DES");
                    generadorDES.init(56);  // El tamaño de la subclave es 56 bits
                    clave = generadorDES.generateKey();

                    // Cifrar el archivo
                    Cipher cifrador = Cipher.getInstance("DES/ECB/PKCS5Padding");
                    cifrador.init(Cipher.ENCRYPT_MODE, clave);

                    byte[] buffer = new byte[1000];
                    byte[] buffercifrado;

                    FileInputStream entrada = new FileInputStream(archivoEntrada);
                    ByteArrayOutputStream salida = new ByteArrayOutputStream();

                    int bytesLeidos = entrada.read(buffer, 0, 1000);
                    while (bytesLeidos != -1) {
                        buffercifrado = cifrador.update(buffer, 0, bytesLeidos);
                        salida.write(buffercifrado);
                        bytesLeidos = entrada.read(buffer, 0, 1000);
                    }

                    buffercifrado = cifrador.doFinal();
                    salida.write(buffercifrado);

                    entrada.close();

                    // Mostrar el archivo cifrado en el JTextArea
                    resultArea.setText("Archivo cifrado exitosamente. Contenido cifrado:\n");
                    resultArea.append(bytesToHex(buffercifrado));

                    // Guardar el archivo cifrado
                    FileOutputStream fileOut = new FileOutputStream(filePath + ".cifrado");
                    fileOut.write(salida.toByteArray());
                    fileOut.close();

                } catch (Exception ex) {
                    resultArea.setText("Error al cifrar el archivo.");
                    ex.printStackTrace();
                }
            }
        });

        // Acción para descifrar el archivo
        decryptButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String filePath = filePathField.getText();
                File archivoEntrada = new File(filePath + ".cifrado");

                if (!archivoEntrada.exists()) {
                    resultArea.setText("El archivo cifrado no existe.");
                    return;
                }

                try {
                    // Desencriptar el archivo
                    Cipher cifrador = Cipher.getInstance("DES/ECB/PKCS5Padding");
                    cifrador.init(Cipher.DECRYPT_MODE, clave);

                    byte[] buffer = new byte[1000];
                    byte[] bufferDescifrado;

                    FileInputStream entradaCifrada = new FileInputStream(archivoEntrada);
                    ByteArrayOutputStream salidaDescifrada = new ByteArrayOutputStream();

                    int bytesLeidos = entradaCifrada.read(buffer, 0, 1000);
                    while (bytesLeidos != -1) {
                        bufferDescifrado = cifrador.update(buffer, 0, bytesLeidos);
                        salidaDescifrada.write(bufferDescifrado);
                        bytesLeidos = entradaCifrada.read(buffer, 0, 1000);
                    }

                    bufferDescifrado = cifrador.doFinal();
                    salidaDescifrada.write(bufferDescifrado);

                    entradaCifrada.close();

                    // Mostrar el archivo descifrado en el JTextArea
                    resultArea.setText("Archivo descifrado exitosamente. Contenido descifrado:\n");
                    resultArea.append(new String(salidaDescifrada.toByteArray()));

                } catch (Exception ex) {
                    resultArea.setText("Error al descifrar el archivo.");
                    ex.printStackTrace();
                }
            }
        });
    }

    // Método para convertir un array de bytes en un string hexadecimal
    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02X ", b));
        }
        return sb.toString();
    }
}
