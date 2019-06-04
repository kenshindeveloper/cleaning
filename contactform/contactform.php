<?php
   $name = $_POST["name"];
   $email = $_POST["email"];
   $subject = $_POST["subject"];
   $message = $_POST["message"];

    $from = "cleaning@gmail.com"; // correo de los panas
    $to = "cleaning@gmail.com"; //correo de los panas s el mismo, ya que se lo envia a si mismo
    // con la info del cliente.
    
    $messageFinal = "name: ".$name."</br>";
    $messageFinal .= "email: ".$email."</br></br>";
    $messageFinal .= $message;
    $headers = "From:" . $from;
    mail($to,$subject,$messageFinal, $headers);
?>