<template>
    <div class="login">
        <form>
            <h3>Sign In</h3>

            <div class="form-group">
                <label>Username</label>
                <input type="username" class="form-control form-control-lg" />
            </div>

            <div class="form-group">
                <label>Password</label>
                <input type="password" class="form-control form-control-lg" />
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