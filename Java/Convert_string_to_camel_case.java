package Java;

class Convert_string_to_camel_case {

    static String toCamelCase(String s) {
        boolean mayus = false;
        String strFinal = "";
        char[] lista = new char[s.length()];
        // Copy character by character into array
        for (int i = 0; i < s.length(); i++) {
            lista[i] = s.charAt(i);
        }

        // Printing content of array
        for (char c : lista) {
            if (c == '-' || c == '_') {
                mayus = true;
                continue;
            }
            if (mayus == true) {
                strFinal += String.valueOf(c).toUpperCase();
                mayus = false;
            } else {
                strFinal += c;
                mayus = false;
            }
        }

        return strFinal;
    }
}