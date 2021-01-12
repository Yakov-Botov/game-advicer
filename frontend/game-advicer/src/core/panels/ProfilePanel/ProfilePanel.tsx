import React from 'react'
import {
    Group,
    Panel,
    PanelHeader,
    SimpleCell,
    Switch,
} from '@vkontakte/vkui'
import { PanelBaseProps } from '..'

/** Панель с информацией о пользователе и настройками приложения */
export const ProfilePanel: React.FC<PanelBaseProps> = React.memo(({ id }) =>
    (
        <Panel id={id}>
            <PanelHeader>Профиль пользователя</PanelHeader>
            <Group>
                <SimpleCell after={<Switch/>}>Темная тема</SimpleCell>
            </Group>
        </Panel>
    ))
