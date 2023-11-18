import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Main {
    public static void main(String[] args) {
        // 正規表現パターンを定義
        String regexPattern = "^[0-9-]+$";

        // テストする文字列
        String inputString = "123-456-7890";

        // 正規表現のパターンをコンパイル
        Pattern pattern = Pattern.compile(regexPattern);

        // マッチャーを作成
        Matcher matcher = pattern.matcher(inputString);

        // マッチングを確認
        if (matcher.matches()) {
            System.out.println("入力文字列はハイフンと半角数字のみです。");
        } else {
            System.out.println("入力文字列にはハイフンと半角数字以外の文字が含まれています。");
        }
    }
}
