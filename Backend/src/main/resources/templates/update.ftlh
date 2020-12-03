<#import "parts/common.ftlh" as c>
<#import "parts/header.ftlh" as h>

<@c.page>
    <@h.page/>
        <form action="" method="post" accept-charset="UTF-8">
            <div class="form-group">
                <label for="color">Weight</label>
                <input type="text" id="color" class="form-control" value="<#if user??>${body.weight!}</#if>"
                       name="weight">
            </div>
            <div class="form-group">
                <label for="color">Height</label>
                <input type="number" id="color" class="form-control" value="<#if user??>${body.height!}</#if>"
                       name="height">
            </div>
            <div class="form-group">
                <label for="age">Age</label>
                <input type="number" id="age" class="form-control" value="<#if user??>${user.body.age!}"</#if> name="age">
            </div>
            <div class="form-group">
                <label for="gender">Purpose</label>
                <select id="gender" name="purpose" class="form-control">
                <#if body.purpose == 0>
                    <option selected value="0">Lose weight</option>
                    <option value="2">Save weight</option>
                    <option value="1">To gain weight</option>
                <#elseif body.purpose == 1>
                    <option value="0">Lose weight</option>
                    <option value="2">Save weight</option>
                    <option selected value="1">To gain weight</option>
                <#else>
                    <option value="0">Lose weight</option>
                    <option selected value="2">Save weight</option>
                    <option value="1">To gain weight</option>
                </#if>
            </select>
            </div>
            <button type="submit" class="btn btn-success">Save</button>
        </form>
    </div>

</@c.page>