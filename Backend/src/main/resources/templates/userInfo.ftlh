<#import "parts/common.ftlh" as c>
<#import "parts/header.ftlh" as h>

<@c.page>
    <@h.page/>

<#if user??>
    <div class="form-group container col-3 mt-5">
        <ul class="list-group">
            <li class="list-group-item">Имя: ${user.name!}</li>
            <li class="list-group-item">Mail: ${user.email!}</li>
            <li class="list-group-item">Пол: ${body.gender!}</li>
            <li class="list-group-item">Возраст: ${body.age!}</li>
            <li class="list-group-item">AMR: ${body.AMR!}</li>
            <li class="list-group-item">BMR: ${body.BMR!}</li>
            <li class="list-group-item">Цель: ${body.purpose!}</li>
            <li class="list-group-item">Рост: ${body.height}</li>
            <li class="list-group-item">Вес: ${body.weight!}</li>
            <li class="list-group-item">Диета: ${body.typeDiet!}</li>
            <li class="list-group-item">Калории: ${body.calRate!}</li>
        </ul>
    </div>

    <div class="container mt-3">
        <table class="table table-sm mt-3 border">
            <thead>
            <tr>
                <th scope="col">Дата</th>
                <th scope="col">Цель</th>
                <th scope="col">Завтрак</th>
                <th scope="col">Обед</th>
                <th scope="col">Ужин</th>
            </tr>
            </thead>
            <tbody>
            <#list rations as ration>
                <tr>
                    <th scope="row">${ration.date!}</th>
                    <#if ration.purpose == 0>
                       <td> Снизить вес </td>
                    <#elseif ration.purpose == 2>
                        <td> Сохранить вес </td>
                    <#elseif ration.purpose == 1>
                        <td> Набрать весь </td>
                    </#if>
                    <td><a href="${ration.breakfast.url!}">${ration.breakfast.id!}</a></td>
                    <td><a href="${ration.lunch.url!}">${ration.lunch.id!}</a></td>
                    <td><a href="${ration.dinner.url!}">${ration.dinner.id!}</a></td>
                </tr>
            </#list>
            </tbody>
        </table>
    </div>
</#if>

</@c.page>