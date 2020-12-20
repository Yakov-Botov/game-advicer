import React from 'react'
import Panel from '@vkontakte/vkui/dist/components/Panel/Panel'
import PanelHeader from '@vkontakte/vkui/dist/components/PanelHeader/PanelHeader'
import Group from '@vkontakte/vkui/dist/components/Group/Group'
import { Cell } from '@vkontakte/vkui'
import { PanelBaseProps } from '..'

export const RandomGamePanel: React.FC<PanelBaseProps> = React.memo(
    ({ id }) => (
        <Panel id={id}>
            <PanelHeader>Случайная игра</PanelHeader>

            <Group title="Navigation Example">
                <Cell>получить случайную игру</Cell>
            </Group>
        </Panel>
    )
)
