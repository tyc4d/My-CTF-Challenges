<?php      
    $host = "mysql";  
    $user = "root";  
    $password = 'mysql_root_password';  
    $db_name = "mydb";  
      
    $conn = mysqli_connect($host, $user, $password, $db_name);  
    
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    // Retrieve input values
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    
    // Query to check if the username and password match
    $sql = "SELECT password FROM users WHERE username='$username'";
    $result = $conn->query($sql);
    $row = mysqli_fetch_assoc($result);
    if ($conn->errno) {
        throw new RuntimeException('mysqli error: ' . mysqli_error($conn));
    }
    if($row["password"]==$_POST['password']){
        // Login successful
        session_start();
        $_SESSION['username'] = $username;
        header('Location: welcome.php');
    
    } else {
        // Login failed, redirect back to login page with an error message
        echo "Failure <br />";
        echo "username , password <br />";
        while ($row = mysqli_fetch_assoc($result)) {
            echo $row["username"] . " , ". $row["password"];
            echo "<br />";
        }
        if(mysqli_fetch_assoc($result)){
            echo "No Result";
        }
        //header('Location: index.html?error=1');
    }


    
    $conn->close();
    ?>
    