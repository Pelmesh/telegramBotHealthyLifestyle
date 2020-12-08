<#import "parts/common.ftlh" as c>
<#import "parts/header.ftlh" as h>

<@c.page>
    <@h.page/>
    <div class="container col-4">
        <form action="" method="post" accept-charset="UTF-8">
            <div class="form-group">
                <label for="color">Вес</label>
                <input type="text" id="color" class="form-control" value="<#if user??>${body.weight!}</#if>"
                       name="weight">
            </div>
            <div class="form-group">
                <label for="color">Рост</label>
                <input type="number" id="color" class="form-control" value="<#if user??>${body.height!}</#if>"
                       name="height">
            </div>
            <div class="form-group">
                <label for="age">Возраст</label>
                <input type="number" id="age" class="form-control" value="<#if user??>${user.body.age!}"</#if> name="age">
            </div>
            <div class="form-group">
                <label for="gender">Цель</label>
                <select id="gender" name="purpose" class="form-control">
                <#if body.purpose == 0>
                    <option selected value="0">Сбросить вес</option>
                    <option value="2">Сохранить вес</option>
                    <option value="1">Набрать вес</option>
                <#elseif body.purpose == 1>
                    <option value="0">Сбросить вес</option>
                    <option value="2">Сохранить вес</option>
                    <option selected value="1">Набрать вес</option>
                <#else>
                    <option value="0">Сбросить вес</option>
                    <option selected value="2">Сохранить вес</option>
                    <option value="1">TНабрать вес</option>
                </#if>
            </select>
            </div>
            <div class="form-group">
                <label for="gender">Образ жизни</label>
                <select id="gender" name="AMR" class="form-control">
                        <option value="1.2">Сидячий образ жизни</option>
                        <option value="1.135">Умеренная активность </option>
                        <option value="1.55">Средняя активность </option>
                        <option value="1.725">Активные люди</option>
                        <option value="1.9">Спортсмены и люди, выполняющие тяжелые физические нагрузки </option>
                </select>
            </div>
            <div class="form-group">
                <label for="gender">Тип диеты</label>
                <select id="gender" name="typeDiet" class="form-control">
                    <option value="normal">Неважно</option>
                    <option value="vegetarian">Вегетарианская еда</option>
                    <option value="vegan">Веганская еда </option>
                    <option value="lenten">Постная еда</option>
                    <option value="diabet">Меню при диабете </option>
                </select>
            </div>
            <button type="submit" class="btn btn-success">Сохранить</button>
        </form>
    </div>
    </div>

</@c.page>