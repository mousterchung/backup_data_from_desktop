$to = "dinshchung@gmail.com";//收件者
$subject = "720 Form";//主旨
$headers = "From: dinshchung@gmail\r\n";//寄件者
$headers .= "Cc: \r\n";//副本
$headers .= "Bcc: \r\n";//密件副本
$headers .= "Reply-To: dinshchung@gmail\r\n";//指定收件者回覆時的預設的信箱
$headers .= "Return-Path: dinshchung@gmail\r\n";//如無設定有時會被mail server 檔下
//信件格式
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";
//信件內容
$message = "<html><body>";
$message .= "php <strong>信件發送</strong>";
$message.="text=".$HTTP_POST_VARS["text"];
$message.="dtl=".$HTTP_POST_VARS["dtl"];
$message.="color=".$HTTP_POST_VARS["color"];
$message .= "</body></html>";
if (mail($to, $subject, $message, $headers)) {
    echo "信件已寄出";
} else {
    echo "信件發送失敗!";
}