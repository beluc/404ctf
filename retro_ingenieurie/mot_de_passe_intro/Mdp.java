/*
 * Decompiled with CFR 0.150.
 */
package chall;

import java.util.Scanner;

public class Mdp {
    public static void main(String[] arrstring) {
        String string = "4/2@PAu<+ViNgg%^5NS`#J\u001fNK<XNW(_";
        Scanner scanner = new Scanner(System.in);
        System.out.print("Mot de passe Admin:");
        String string2 = scanner.nextLine();
        if (string.equals(Mdp.hide(string2))) {
            System.out.println("Bienvenue Admin");
        } else {
            System.out.println("Au revoir non admin");
        }
    }

    static String hide(String string) {
        Object object = "";
        for (int i = 0; i < string.length(); ++i) {
            char c = string.charAt(i);
            c = (char)(c - i);
            c = (char)(c % 128);
            object = (String)object + c;
        }
        return object;
    }
}
