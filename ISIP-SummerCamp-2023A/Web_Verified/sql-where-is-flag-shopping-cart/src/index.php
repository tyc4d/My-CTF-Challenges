<?php
session_start();
require_once("dbcontroller.php");
$db_handle = new DBController();
if(!empty($_POST["action"])) {
switch($_POST["action"]) {
	case "add":
		if(!empty($_POST["quantity"])) {
			$qq = "SELECT * FROM tblproduct WHERE code='" . $_POST["code"] . "'";
			$productByCode = $db_handle->runQuery($qq);
			echo "<div style='margin-left: 40px;margin-top:1%;'><h3>開發偵錯用(記得關閉by宸宸 ): " . $qq . "</h3></div>";
			$itemArray = array($productByCode[0]["code"]=>array('name'=>$productByCode[0]["name"], 'code'=>$productByCode[0]["code"], 'quantity'=>$_POST["quantity"], 'price'=>$productByCode[0]["price"], 'image'=>$productByCode[0]["image"]));
			
			if(!empty($_SESSION["cart_item"])) {
				if(in_array($productByCode[0]["code"],array_keys($_SESSION["cart_item"]))) {
					foreach($_SESSION["cart_item"] as $k => $v) {
							if($productByCode[0]["code"] == $k) {
								if(empty($_SESSION["cart_item"][$k]["quantity"])) {
									$_SESSION["cart_item"][$k]["quantity"] = 0;
								}
								$_SESSION["cart_item"][$k]["quantity"] += $_POST["quantity"];
							}
					}
				} else {
					$_SESSION["cart_item"] = array_merge($_SESSION["cart_item"],$itemArray);
				}
			} else {
				$_SESSION["cart_item"] = $itemArray;
			}
		}
	break;
	case "remove":
		if(!empty($_SESSION["cart_item"])) {
			foreach($_SESSION["cart_item"] as $k => $v) {
					if($_POST["code"] == $k)
						unset($_SESSION["cart_item"][$k]);				
					if(empty($_SESSION["cart_item"]))
						unset($_SESSION["cart_item"]);
			}
		}
	break;
	case "empty":
		unset($_SESSION["cart_item"]);
	break;	
}
}
?>
<HTML>
<HEAD>
<TITLE>來買FLAG吧</TITLE>
<link href="style.css" type="text/css" rel="stylesheet" />
</HEAD>
<BODY>
<div id="shopping-cart">
<h3>我的購物車</h3>
<?php
if(isset($_SESSION["cart_item"])){
    $total_quantity = 0;
    $total_price = 0;
	
?>	
<table class="tbl-cart" cellpadding="10" cellspacing="1">
<tbody>
<tr>
<th style="text-align:left;">名稱</th>
<th style="text-align:left;">商品代號</th>
<th style="text-align:right;" width="5%">數量</th>
<th style="text-align:right;" width="10%">單價</th>
<th style="text-align:right;" width="10%">總價</th>
<th style="text-align:center;" width="5%">移除</th>
</tr>	
<?php		
    foreach ($_SESSION["cart_item"] as $item){
        $item_price = $item["quantity"]*$item["price"];
		
		?>
				<tr>
				<td><img src="<?php echo $item["image"]; ?>" class="cart-item-image" /><?php echo $item["name"]; ?></td>
				<td><?php echo $item["code"]; ?></td>
				<td style="text-align:right;"><?php echo $item["quantity"]; ?></td>
				<td style="text-align:right;"><?php echo "$ ".$item["price"]; ?></td>
				<td style="text-align:right;"><?php echo "$ ". number_format($item_price,2); ?></td>
				<form method="post" action="index.php">
					<input type="hidden" name="action" value="remove">
					<input type="hidden" name="code" value='<?php echo $item["code"]; ?>'>
					<td style="text-align:center;"><input value="刪除" type="submit" class="btnRemoveAction" /></td>
				</form>
				</tr>
				<?php
				$total_quantity += $item["quantity"];
				$total_price += ($item["price"]*$item["quantity"]);
		}
		?>

<tr>
<td colspan="2" align="right">總價為:</td>
<td align="right"><?php echo $total_quantity; ?></td>
<td align="right" colspan="2"><strong><?php echo "$ ".number_format($total_price, 2); ?></strong></td>
<td></td>
</tr>
</tbody>
</table>		
  <?php
} else {
?>
<div class="no-records">你還沒放任何東西到購物車喔</div>
<?php 
}
?>
</div>

<div id="product-grid">
	<div class="txt-heading"><h3>商品</div>
	<?php
	$product_array = $db_handle->runQuery("SELECT * FROM tblproduct ORDER BY id ASC");
	if (!empty($product_array)) { 
		foreach($product_array as $key=>$value){
		if($key == 4){

		}
		else{
	?>
		<div class="product-item">
			<form method="post" action="index.php">
			<div class="product-image" style="text-align: center;margin-top: 20px;"><img src="<?php echo $product_array[$key]["image"]; ?>"></div>
			<div class="product-tile-footer">
			<input type="hidden" name="action" value="add">
			<input type="hidden" name="code" value="<?php echo $product_array[$key]["code"]; ?>">

			<div class="product-title"><?php echo $product_array[$key]["name"]; ?></div>
			<div class="product-price"><?php echo "$".$product_array[$key]["price"]; ?></div>
			<div class="cart-action"><input type="text" class="product-quantity" name="quantity" value="1" size="2" /><input type="submit" value="加到購物車" class="btnAddAction" /></div>
			</div>
			</form>
		</div>
	<?php
		
		}
	}
}
	?>
</div>
</BODY>
</HTML>