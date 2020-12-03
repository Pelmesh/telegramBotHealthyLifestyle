<#import "parts/common.ftlh" as c>
<#import "parts/header.ftlh" as h>

<@c.page>
    <@h.page/>

    <div class="container mt-5">
        <div class="row justify-content-center align-items-center">
            <form class="text-center border border-light p-5 col-4" action="" method="post">
                <label for="text">Login</label>
                <input type="text" class="form-control"
                       placeholder="Username" name="username">
                <span class=" invalid-feedback" id="form__error">Example name: User, user20</span>
                <input type="password" class="form-control mt-4" placeholder="Password"
                       aria-describedby="defaultRegisterFormPasswordHelpBlock" name="password" required pattern="^[А-ЯА-яA-Za-z0-9]{1,15}$">
                <span class=" invalid-feedback" id="form__error">Example password: mrCmTF1567, YRTbsq23fsc</span>
                <button class="btn btn-outline-info btn-rounded btn-block my-4 waves-effect z-depth-0" type="submit">
                    Sign In
                </button>
            </form>
        </div>
    </div>

</@c.page>