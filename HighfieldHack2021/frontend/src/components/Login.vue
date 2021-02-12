<template>
    <div class="login">
        <form>
            <h3>Sign In</h3>

            <div class="form-group">
                <label><b>Username</b></label>
                <input name="username" type="text" class="form-control form-control-lg" />
            </div>

            <div class="form-group">
                <label><b>Password</b></label>
                <input name="password" type="password" class="form-control form-control-lg" />
            </div>

            <button type="submit" class="btn btn-dark btn-lg btn-block">Sign In</button>
        </form>
    </div>
</template>

<script>
    export default {
        data() {
            return {}
        }
    }
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
  padding: 10px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
label {
    padding: 10px;
}
input[type=text], input[type=password] {
  width: 50%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
  font-size: 16px;
  border-radius: 25%;
}
</style>