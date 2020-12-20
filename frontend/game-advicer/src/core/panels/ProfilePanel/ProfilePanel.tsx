import React from 'react'
import {Cell, Panel, PanelHeader} from '@vkontakte/vkui'
import { PanelBaseProps } from '..'

export const ProfilePanel: React.FC<PanelBaseProps> = React.memo(({ id }) => {
    return (
        <Panel id={id}>
            <PanelHeader>Профиль пользователя</PanelHeader>
            <Cell>Профиль пользователя</Cell>
        </Panel>
    )
})
